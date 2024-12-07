import pygame
from local import *
from scenes.animal import Animal
from time import sleep
from music import Playmusic



class PlayingScene:
    def __init__(self, screen, manager):
        self.cnt = 0
        # Biến để theo dõi thời gian
        self.start_time = pygame.time.get_ticks()

        self.screen = screen
        self.manager = manager
        self.bg_image = pygame.image.load("assets/play_background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


        self.button_settings = pygame.image.load("assets/setting_icon.png")
        self.button_sound_on = pygame.image.load("assets/sound_icon.png")
        self.button_sound_off = pygame.image.load("assets/mute_icon.png")


        self.button_settings = pygame.transform.scale(self.button_settings, (80, 80))
        self.button_sound_on = pygame.transform.scale(self.button_sound_on, (80, 80))
        self.button_sound_off = pygame.transform.scale(self.button_sound_off, (80, 80))

        self.tiles = [Animal(i) for i in range(0, NUM_TILES_TOTAL)]
        self.current_images_displayed = []

        self.music_player = Playmusic()
        self.music_player.play_play_sound()


        self.buttons = {
            "settings": self.button_settings.get_rect(topright=(SCREEN_WIDTH - 10, 0)),
            "sound": self.button_sound_on.get_rect(topright=(SCREEN_WIDTH - 100, 0)),
        }
        self.sound_on = True

        self.level = self.manager.get_selected_level()


    @staticmethod
    def find_index_from_xy(x, y):
        adjusted_x = x - SCREEN_WIDTH // 2 + (NUM_TILES_COL * IMAGE_SIZE) // 2
        adjusted_y = (y - 30) - SCREEN_HEIGHT // 2 + (NUM_TILES_ROW * IMAGE_SIZE) // 2
        row = adjusted_y // IMAGE_SIZE
        col = adjusted_x // IMAGE_SIZE
        if row < 0 or col < 0 or row >= NUM_TILES_ROW  or col >= NUM_TILES_COL:
            return -1, -1, -1
        index = row * NUM_TILES_COL + col
        return row, col, index




    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Nhấn ESC để thoát
                    pygame.quit()
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    mouse_pos = event.pos
                    if self.buttons["settings"].collidepoint(mouse_pos):
                        self.manager.change_scene("settings_play")
                    elif self.buttons["sound"].collidepoint(mouse_pos):
                        self.sound_on = not self.sound_on
                        self.music_player.toggle_sound()

                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    row, col, index = self.find_index_from_xy(mouse_x, mouse_y)
                    if index != -1 and index < len(self.tiles) and not self.tiles[index].skip:
                        if index not in self.current_images_displayed and len(self.current_images_displayed) < 2:
                            self.current_images_displayed.append(index)

            if event.type in [pygame.MOUSEMOTION, pygame.MOUSEWHEEL]:
                continue

        return True


    def update(self):
        pass


    def render(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.button_settings, self.buttons["settings"])
        if self.sound_on:
            self.screen.blit(self.button_sound_on, self.buttons["sound"])
        else:
            self.screen.blit(self.button_sound_off, self.buttons["sound"])

        total_skipped = 0
        total_width = NUM_TILES_COL * IMAGE_SIZE
        total_height = NUM_TILES_ROW * IMAGE_SIZE
        center_x = (SCREEN_WIDTH - total_width) // 2
        center_y = (SCREEN_HEIGHT - total_height) // 2 + 30

        for row in range(NUM_TILES_ROW):
            for col in range(NUM_TILES_COL):
                index = row * NUM_TILES_COL + col
                tile = self.tiles[index]

                current_image = tile.image if index in self.current_images_displayed else tile.box
                if not tile.skip:
                    x_pos = center_x + col * IMAGE_SIZE + MARGIN
                    y_pos = center_y + row * IMAGE_SIZE + MARGIN
                    self.screen.blit(current_image, (x_pos, y_pos))
                else:
                    total_skipped += 1

        elapsed_time = pygame.time.get_ticks() - self.start_time  # Thời gian từ khi bắt đầu
        seconds = elapsed_time // 1000  # Chuyển đổi thời gian từ milliseconds sang seconds
        font = pygame.font.SysFont("Arial", 50)
        time_text = font.render(f"{seconds}s", True, (25, 25, 255))  # Màu trắng cho văn bản
        self.screen.blit(time_text, (200, 10))  # Vẽ thời gian ở góc trên bên trái


        if self.level == 2:
            if self.cnt > 3 or seconds/60 > 3:
                self.manager.change_scene("end_lose")
        elif self.level == 1:
            if seconds/60 > 3:
                self.manager.change_scene("end_lose")


        pygame.display.flip()

        if len(self.current_images_displayed) == 2:
            idx1, idx2 = self.current_images_displayed
            sleep(0.2)
            if self.tiles[idx1].name == self.tiles[idx2].name:
                self.tiles[idx1].skip = True
                self.tiles[idx2].skip = True
            else:
                self.current_images_displayed = []
                self.cnt += 1
                print(self.cnt)
            sleep(0.2)
            self.current_images_displayed = []



        if total_skipped == len(self.tiles):
            self.manager.change_scene("end_win")
