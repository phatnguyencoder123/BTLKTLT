import pygame
from local import *


class SettingsScene:
    def __init__(self, screen, manager, button_data):
        self.screen = screen
        self.manager = manager
        self.bg_image = pygame.image.load("assets/setting_background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.font = pygame.font.SysFont("Arial", 40)
        self.buttons = {}
        self.button_images = {}

        # Khởi tạo các nút từ button_data
        for key, data in button_data.items():
            image = pygame.image.load(data["image"])
            image = pygame.transform.scale(image, data["size"])
            rect = image.get_rect(center=data["position"])
            self.button_images[key] = image
            self.buttons[key] = rect

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    mouse_pos = event.pos
                    for key, rect in self.buttons.items():
                        if rect.collidepoint(mouse_pos):
                            action = self.get_action(key)
                            if action:
                                action()
        return True

    def get_action(self, key):
        """Phương thức để trả về hành động tương ứng với nút"""
        return None

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.bg_image, (0, 0))
        for key, rect in self.buttons.items():
            self.screen.blit(self.button_images[key], rect)


class OpenSettingScene(SettingsScene):
    def __init__(self, screen, manager):
        button_data = {
            "resume": {"image": "assets/resume.png", "size": (200, 100), "position": (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200)},
            "level": {"image": "assets/level_icon.png", "size": (100, 100), "position": (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300)},
            "quit": {"image": "assets/quit.png", "size": (100, 100), "position": (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 400)},
        }
        super().__init__(screen, manager, button_data)

    def get_action(self, key):
        if key == "resume":
            return lambda: self.manager.change_scene("opening")
        elif key == "level":
            return lambda: self.manager.change_scene("level")
        elif key == "quit":
            return lambda: (pygame.quit(), exit())


class PlaySettingScene(SettingsScene):
    def __init__(self, screen, manager):
        button_data = {
            "restart": {"image": "assets/restart.png", "size": (200, 100), "position": (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120)},
            "home": {"image": "assets/home_icon.png", "size": (100, 100), "position": (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200)},
            "resume": {"image": "assets/resume.png", "size": (100, 100), "position": (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300)},
        }
        super().__init__(screen, manager, button_data)

    def get_action(self, key):
        if key == "restart":
            return lambda: self.manager.change_scene("play")
        elif key == "home":
            return lambda: self.manager.change_scene("opening")
        elif key == "resume":
            return lambda: self.manager.change_scene("play_back")
