import pygame
from local import *
from music import Playmusic

class EndGameScene:
    def __init__(self, screen, manager, bg_image, sound_func):
        self.screen = screen
        self.manager = manager
        self.bg_image = pygame.transform.scale(pygame.image.load(bg_image), (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Load and resize buttons
        self.button_play_again = pygame.transform.scale(pygame.image.load("assets/restart.png"), (180, 80))
        self.button_main_menu = pygame.transform.scale(pygame.image.load("assets/home_icon.png"), (180, 80))
        self.button_sound_on = pygame.transform.scale(pygame.image.load("assets/sound_icon.png"), (80, 80))
        self.button_sound_off = pygame.transform.scale(pygame.image.load("assets/mute_icon.png"), (80, 80))

        self.buttons = {
            "play_again": self.button_play_again.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)),
            "main_menu": self.button_main_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)),
            "sound": self.button_sound_on.get_rect(topright=(SCREEN_WIDTH - 100, 10)),
        }

        self.sound_on = True
        self.music_player = Playmusic()
        sound_func(self.music_player)  # Call the sound function for either victory or game over

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # ESC to quit
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    mouse_pos = event.pos
                    if self.buttons["play_again"].collidepoint(mouse_pos):
                        self.manager.change_scene("play")
                    elif self.buttons["main_menu"].collidepoint(mouse_pos):
                        self.manager.change_scene("opening")
                    elif self.buttons["sound"].collidepoint(mouse_pos):
                        self.sound_on = not self.sound_on
                        self.music_player.toggle_sound()

        return True

    def render(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.button_play_again, self.buttons["play_again"])
        self.screen.blit(self.button_main_menu, self.buttons["main_menu"])
        sound_button = self.button_sound_on if self.sound_on else self.button_sound_off
        self.screen.blit(sound_button, self.buttons["sound"])

class CongratulationsScene(EndGameScene):
    def __init__(self, screen, manager):
        # Load the correct background and play victory sound
        super().__init__(screen, manager, "assets/end_background.jpg", self.play_victory_sound)

    @staticmethod
    def play_victory_sound(music_player):
        music_player.play_win_sound()  # Play victory sound for the win scene

    def update(self):
        pass


class GameOverScene(EndGameScene):
    def __init__(self, screen, manager):
        # Load the correct background and play game over sound
        super().__init__(screen, manager, "assets/start_background.png", self.play_game_over_sound)

    @staticmethod
    def play_game_over_sound(music_player):
        music_player.play_lose_sound()  # Play game over sound for the loose scene

    def update(self):
        pass
