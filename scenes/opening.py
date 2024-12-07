import pygame
from local import *
from music import Playmusic

class OpeningScene:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        self.bg_image = pygame.image.load("assets/start_background.png")  # Tải ảnh nền
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Thay đổi kích thước ảnh nền

        # Tải ảnh nút
        self.button_play = pygame.image.load("assets/play_icon.png")
        self.button_settings = pygame.image.load("assets/setting_icon.png")
        self.button_sound_on = pygame.image.load("assets/sound_icon.png")
        self.button_sound_off = pygame.image.load("assets/mute_icon.png")

        # Thay đổi kích thước các nút
        self.button_play = pygame.transform.scale(self.button_play, (180, 80))
        self.button_settings = pygame.transform.scale(self.button_settings, (80, 80))
        self.button_sound_on = pygame.transform.scale(self.button_sound_on, (80, 80))
        self.button_sound_off = pygame.transform.scale(self.button_sound_off, (80, 80))

        self.buttons = {
            "play": self.button_play.get_rect(center =(SCREEN_WIDTH // 2 , SCREEN_HEIGHT - 100)),
            "settings": self.button_settings.get_rect(topright=(SCREEN_WIDTH - 10, 10)),
            "sound": self.button_sound_on.get_rect(topright=(SCREEN_WIDTH - 100, 10)),
        }

        self.sound_on = True

        self.music_player = Playmusic()
        self.music_player.play_open_sound()



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
                    if self.buttons["play"].collidepoint(mouse_pos):
                        self.manager.change_scene("play")
                    elif self.buttons["settings"].collidepoint(mouse_pos):
                        self.manager.change_scene("settings_open")
                    elif self.buttons["sound"].collidepoint(mouse_pos):
                        self.sound_on = not self.sound_on
                        self.music_player.toggle_sound()

        return True

    def update(self):
        pass

    def render(self):
        # Vẽ ảnh nền
        self.screen.blit(self.bg_image, (0, 0))

        # Vẽ các nút
        self.screen.blit(self.button_play, self.buttons["play"])
        self.screen.blit(self.button_settings, self.buttons["settings"])
        if self.sound_on:
            self.screen.blit(self.button_sound_on, self.buttons["sound"])
        else:
            self.screen.blit(self.button_sound_off, self.buttons["sound"])
