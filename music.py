import pygame

class Playmusic:
    def __init__(self):
        # Đặt đường dẫn đến nhạc nền cho từng màn hình
        self.open_sound = "assets/opening_sound.mp3"  # Nhạc nền cho màn hình Open
        self.play_sound = "assets/playing_sound.mp3"  # Nhạc nền cho màn hình Play
        self.win_sound = "assets/winning_sound.mp3"  # Nhạc nền cho màn hình Win
        self.lose_sound = "assets/lose_sound.mp3"  # Nhạc nền cho màn hình Lose

        self.is_playing = False

    def play_open_sound(self):
        """Phát nhạc nền cho màn hình Open"""
        if not self.is_playing:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.open_sound)
            pygame.mixer.music.play(-1, 0.0)  # Phát nhạc nền lặp lại vô hạn
            self.is_playing = True

    def play_play_sound(self):
        """Phát nhạc nền cho màn hình Play"""
        if not self.is_playing:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.play_sound)
            pygame.mixer.music.play(-1, 0.0)  # Phát nhạc nền lặp lại vô hạn
            self.is_playing = True

    def play_win_sound(self):
        """Phát nhạc nền cho màn hình Win"""
        if not self.is_playing:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.win_sound)
            pygame.mixer.music.play(-1, 0.0)  # Phát nhạc nền lặp lại vô hạn
            self.is_playing = True

    def play_lose_sound(self):
        """Phát nhạc nền cho màn hình Lose"""
        if not self.is_playing:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.lose_sound)
            pygame.mixer.music.play(-1, 0.0)  # Phát nhạc nền lặp lại vô hạn
            self.is_playing = True

    def stop_music(self):
        """Dừng nhạc nền"""
        pygame.mixer.music.stop()
        self.is_playing = False

    def toggle_sound(self):
        """Bật/Tắt âm thanh"""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
