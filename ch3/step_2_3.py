from PIL import Image
from step_1_1 import IMG_DIR # 이전에 작성한 모듈을 불러옵니다.

SIZE = (500, 500)
img = Image.open(IMG_DIR / "img_001.jpg")
img_resize = img.resize(SIZE)
img_black = Image.new(mode="RGBA", size=SIZE, color=(0, 0, 0, 153)) # size="SIZE", size=SIZE 차이?
img_comp = Image.alpha_composite(img_resize.convert("RGBA"), img_black)
img_comp

# 함수별 이미지 크기 변경
from PIL import Image, ImageOps
from step_1_1 import IN_DIR, OUT_DIR # 이전에 작성한 모듈을 불러옵니다.

SIZE = (500, 500)
img = Image.open(IN_DIR / "breaking.jpg")
img.resize(SIZE).save(OUT_DIR / "1_resize.jpg")
ImageOps.contain(img, SIZE).save(OUT_DIR / "2_contain.jpg")
ImageOps.cover(img, SIZE).save(OUT_DIR / "3_cover.jpg")
ImageOps.fit(img, SIZE).save(OUT_DIR / "4_fit.jpg")
ImageOps.pad(img, SIZE, color=(0, 0, 0)).save(OUT_DIR / "5_pad.jpg")