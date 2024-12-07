import pygame
from local import *

class LevelScene:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        self.font = pygame.font.SysFont("Arial", 40)
        self.buttons = {
            "level1": pygame.Rect(SCREEN_WIDTH // 2 - 100, 200, 200, 50),
            "level2": pygame.Rect(SCREEN_WIDTH // 2 - 100, 300, 200, 50),
            "back": pygame.Rect(SCREEN_WIDTH // 2 - 100, 400, 200, 50),
        }

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    mouse_pos = event.pos
                    if self.buttons["level1"].collidepoint(mouse_pos):
                        self.manager.selected_level = 1  # Lưu level 1
                        print("Level 1 selected!")
                    elif self.buttons["level2"].collidepoint(mouse_pos):
                        self.manager.selected_level = 2  # Lưu level 2
                        print("Level 2 selected!")
                    elif self.buttons["back"].collidepoint(mouse_pos):
                        self.manager.change_scene("opening")
        return True

    def update(self):
        pass

    def render(self):
        self.screen.fill((150, 150, 150))
        self.draw_button("Level 1", self.buttons["level1"])
        self.draw_button("Level 2", self.buttons["level2"])
        self.draw_button("Back", self.buttons["back"])

    def draw_button(self, text, rect):
        pygame.draw.rect(self.screen, (200, 200, 200), rect)
        label = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(label, label.get_rect(center=rect.center))
