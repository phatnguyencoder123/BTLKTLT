import os

SCREEN_WIDTH, SCREEN_HEIGHT = 1080,600
FPS = 80

IMAGE_SIZE = 70
NUM_TILES_COL = 8
NUM_TILES_ROW = 7
NUM_TILES_TOTAL = NUM_TILES_COL * NUM_TILES_ROW
MARGIN = 5

ASSET_DIR =   r'C:\Users\LENOVO\BTLKTLT\assets\animal'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 28