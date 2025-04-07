# 이미지 정보
from PIL import Image
from step_1_1 import IMG_DIR # 이전에 작성한 모듈을 불러옵니다.

img = Image.open(IMG_DIR / "img_001.jpg")
print(f"{img.size=}, {img.format=}, {img.mode=}")

# 이미지 크기 변경
SIZE = (500, 500)
img_resize = img.resize(SIZE)
print(f"{img_resize.size=}")
img_resize

# 이미지 비율을 유지하면서 크기 변경
from PIL import ImageOps

img_cont = ImageOps.contain(img, SIZE)
print(f"{img_cont.size=}")
img_cont