import random
from pygame import image, transform
from local import *
animals_count = dict((a, 0) for a in ASSET_FILES)


def available_animals():
    available = [animal for animal, count in animals_count.items() if count < 2]
    if not available:
        # Reset lại số lượng động vật khi tất cả đều đã được chọn đủ số lần
        print("Đã chọn hết động vật, reset lại danh sách!")
        reset_animals_count()
        available = [animal for animal, count in animals_count.items() if count < 2]
    return available


def reset_animals_count():
    global animals_count
    animals_count = dict((a, 0) for a in ASSET_FILES)


class Animal:
    def __init__(self, index):
        self.index = index

        available = available_animals()
        if not available:  # Nếu không còn động vật để chọn, dừng lại hoặc xử lý
            raise ValueError("Không còn động vật nào có thể chọn!")

        self.name = random.choice(available)
        self.image_path = os.path.join(ASSET_DIR, self.name)
        self.row = index // NUM_TILES_ROW
        self.col = index % NUM_TILES_COL
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (IMAGE_SIZE - 2 * MARGIN, IMAGE_SIZE - 2 * MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))
        animals_count[self.name] += 1

