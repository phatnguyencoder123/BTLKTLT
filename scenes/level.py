import pygame
from local import *


class LevelScene:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager

        # Tải ảnh nền
        self.bg_image = pygame.image.load("assets/level_background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Trạng thái level hiện tại
        self.selected_level = None  # Chưa chọn level nào

        # Đường dẫn hình ảnh
        self.icons = {
            "easy": pygame.image.load("assets/easy_icon.png"),
            "easy_selected": pygame.image.load("assets/easyselect_icon.png"),
            "hard": pygame.image.load("assets/hard_icon.png"),
            "hard_selected": pygame.image.load("assets/hardselect_icon.png"),
            "back": pygame.image.load("assets/home_icon.png"),
        }

        # Chỉnh kích thước nút
        self.icons["easy"] = pygame.transform.scale(self.icons["easy"], (300, 120))
        self.icons["easy_selected"] = pygame.transform.scale(self.icons["easy_selected"], (300, 120))
        self.icons["hard"] = pygame.transform.scale(self.icons["hard"], (300, 120))
        self.icons["hard_selected"] = pygame.transform.scale(self.icons["hard_selected"], (300, 120))
        self.icons["back"] = pygame.transform.scale(self.icons["back"], (100, 100))

        # Đặt vị trí cho các nút
        self.level1_rect = self.icons["easy"].get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        self.level2_rect = self.icons["hard"].get_rect(center=(SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT // 2))
        self.back_rect = self.icons["back"].get_rect(center=(SCREEN_WIDTH // 2, 400))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    mouse_pos = event.pos
                    if self.level1_rect.collidepoint(mouse_pos):
                        self.selected_level = 1
                        self.manager.selected_level = 1  # Lưu level 1
                        print("Level 1 selected!")
                    elif self.level2_rect.collidepoint(mouse_pos):
                        self.selected_level = 2
                        self.manager.selected_level = 2  # Lưu level 2
                        print("Level 2 selected!")
                    elif self.back_rect.collidepoint(mouse_pos):
                        self.manager.change_scene("opening")
        return True

    def update(self):
        pass

    def render(self):
        # Vẽ ảnh nền
        self.screen.blit(self.bg_image, (0, 0))

        # Cập nhật hình ảnh của nút level theo trạng thái
        if self.selected_level == 1:
            level1_image = self.icons["easy_selected"]
            level2_image = self.icons["hard"]
        elif self.selected_level == 2:
            level1_image = self.icons["easy"]
            level2_image = self.icons["hard_selected"]
        else:
            level1_image = self.icons["easy"]
            level2_image = self.icons["hard"]

        # Vẽ các nút
        self.screen.blit(level1_image, self.level1_rect.topleft)
        self.screen.blit(level2_image, self.level2_rect.topleft)
        self.screen.blit(self.icons["back"], self.back_rect.topleft)
