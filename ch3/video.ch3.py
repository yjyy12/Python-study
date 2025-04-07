from pathlib import Path # Path 패키지 사용하여 폴더 만들기

WORK_DIR = Path(__file__).parent # WORK_DIR 변수에 현재 작업폴더의 경로 저장
IMG_DIR = WORK_DIR / "img" # IMG_DIR 변수에 이미지 폴더의 경로를 저장 
IN_DIR = WORK_DIR / "input"
OUT_DIR = WORK_DIR / "output"
IMG_DIR.mkdir(exist_ok=True) # mkdir변수를 사용해 각각의 폴더 생성
IN_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)

# 이미지 불러오기
from PIL import Image #필로우 패키지의 이미지 불러오기

IMG_1 = IMG_DIR / "img_001.jpg" # 해당 이미지의 경로를 변수로 저장
Image.open(IMG_1) # 이미지함수의 오픈함수를 사용해서 이미지 객체로 불러오기
img = Image.open(IMG_1) # 이미지 객체를 변수에 저장
img.rotate(45) # 이미지 회전

# 이미지에 문자열 추가
from PIL import ImageDraw # 이미지 draw 모듈 불러오기

ImageDraw.Draw(img) #이미지드로우 객체 생성
draw = ImageDraw.Draw(img) #이미지드로우 객체 생성 후 변수에 저장
draw.text(xy=(0,200), text="Hello, World!", font_size=100, fill=(0, 0, 0)) #커서 올려놓으면 정보가 나오는데, xy변수와 text변수가 가장 중요(xy=출력될 위치, text=출력될 텍스트)
img

#이미지 정보 확인
IMG_2 = IMG_DIR / "img_002.jpg" # 2번 이미지 경로를 저장
Image.open(IMG_2)
img = Image.open(IMG_2)
img.filename #파일 이름을 포함한 전체 경로 확인
img.size
img.mode #이미지의 색상모드를 확인 가능

#이미지 크기 변경
img.resize((500, 500))
img.resize((500, 500)).size #크기 변경됐는지 확인하는 방법
img_resize = img.resize((500, 500)) #변경된 결과를 변수에 저장
img.size, img_resize.size #이미지 객체의 resize함수는 원본이미지를 건들이지 않고 새로운 객체를 생성함

# 이미지 변경 시 가로세로 비율 유지
img
img_resize

from PIL import ImageOps

ImageOps.contain(img, (500, 500)) #원본 비율과 동일하게 변경
ImageOps.contain(img, (500, 500)).size #이미지 사이즈 확인

# 이미지 생성
Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255, 100)) #알파채널이 적용되지 않음 
Image.new(mode="RGBA", size=(100, 100), color=(255, 255, 255, 100)) #mode를 변경하면(RGBA) 색상이 변경됌

# 이미지 합성
Image.alpha_composite(img, Image.new(mode="RGBA", size=img.size, color=(255, 255, 255, 100))) #에러남 왜냐면 img.mode가 RGB라서 -> convert함수 써서 바꿔야함


img.mode
img.convert("RGBA").mode #이미지 모드의 색상모드 변경
Image.alpha_composite(img.convert("RGBA"), Image.new(mode="RGBA", size=img.size, color=(255, 255, 255, 100))) #원본 사진에 하얀색 모드 합성된 결과값

Image.alpha_composite(img.convert("RGBA"), Image.new(mode="RGBA", size=img.size, color=(0, 0, 0, 100))) #원본 사진에 검정색 모드 합성된 결과값

# 이미지 가로 배치
path_sorted = sorted(IMG_DIR.glob("*.jpg")) #정렬하여 리스트로 반환
start_x, start_y = 0, 0
img_bg = Image.new(mode="RGB", size=(500*len(path_sorted), 500))# 베경이미지 만들기
for path_img in path_sorted:
     img_raw = Image.open(path_img)
     img_fit = ImageOps.fit(img_raw, (500, 500)) # 모든 이미지의 크기를 500, 500으로 변환
     img_bg.paste(img_fit, (start_x, start_y))
     start_x += 500 
     print(path_img, img_raw.size, img_fit.size) # 저장된 이미지 위치와 사이즈 확인
 img_bg.save(OUT_DIR / "img_bg_1.png")

# 5행 8열로 이미지 배치하기
start_x, start_y = 0, 0
img_bg = Image.new(mode="RGB", size=(500*8, 500*5))# 베경이미지 만들기
for path_img in path_sorted:
     img_raw = Image.open(path_img)
     img_fit = ImageOps.fit(img_raw, (500, 500)) # 모든 이미지의 크기를 500, 500으로 변환
     img_bg.paste(img_fit, (start_x, start_y))
     start_x += 500 
     if start_x >= 500 * 8:
          start_x = 0
          start_y += 500
 img_bg.save(OUT_DIR / "img_bg_2.png")

# 이미지에 문자열 추가
from PIL import ImageFont

font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", 100)

draw = ImageDraw.Draw(img_bg) #이미지 draw 객체 반환
draw.text(xy=(0, 0), text="발리 여행 사진", fill=(255, 255, 255), font=font) # 이미지에 문자열 추가
img_bg

bbox = font.getbbox("발리 여행 사진")

draw.rectangle(xy=bbox, fill=(0, 0, 0))
img_bg

draw.text(xy=(0, 0), text="발리 여행 사진", fill=(255, 255, 255), font=font) # 이미지에 문자열 추가
img_bg

