import pygame
from scenes.opening import OpeningScene
from scenes.settings import OpenSettingScene
from scenes.settings import PlaySettingScene
from scenes.level import LevelScene
from scenes.playing import PlayingScene
from scenes.ending import CongratulationsScene
from scenes.ending import GameOverScene
from local import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multi-Screen Example")


class SceneManager:
    def __init__(self):
        self.scenes = {}  # Khởi tạo dictionary rỗng cho các scene
        self.current_scene = "opening"  # Cảnh hiện tại bắt đầu là opening
        self.load_scene(self.current_scene)  # Tải cảnh đầu tiên khi bắt đầu
        self.selected_level = None  # Lưu level được chọn

    def get_selected_level(self):
        return self.selected_level


    def load_scene(self, scene_name):
        """ Tải cảnh mới khi chuyển tới """
        if scene_name == "opening":
            self.scenes[scene_name] = OpeningScene(screen, self)
        elif scene_name == "settings_open":
            self.scenes[scene_name] = OpenSettingScene(screen, self)
        elif scene_name == "settings_play":
            self.scenes[scene_name] = PlaySettingScene(screen, self)
        elif scene_name == "level":
            self.scenes[scene_name] = LevelScene(screen, self)
        elif scene_name == "play":
            self.scenes[scene_name] = PlayingScene(screen, self)
        elif scene_name == "end_lose" :
            self.scenes[scene_name] = GameOverScene(screen, self)
        elif scene_name == "end_win":
            self.scenes[scene_name] = CongratulationsScene(screen, self)

    def change_scene(self, scene_name):
        """ Chuyển sang cảnh mới và tải lại nếu cần """
        # Nếu cảnh hiện tại đã có, hủy bỏ nó
        if self.current_scene in self.scenes:
            del self.scenes[self.current_scene]

        # Cập nhật cảnh hiện tại và tải cảnh mới
        self.current_scene = scene_name
        if scene_name not in self.scenes:
            self.load_scene(scene_name)

    def run(self):
        """ Chạy vòng lặp chính của chương trình """
        clock = pygame.time.Clock()
        running = True
        while running:
            current_scene = self.scenes[self.current_scene]
            running = current_scene.handle_events()
            current_scene.update()
            current_scene.render()
            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    manager = SceneManager()
    manager.run()
    pygame.quit()
