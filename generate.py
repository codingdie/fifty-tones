# -*- coding: utf-8 -*-  

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母:
chars=u"あいうえおかきくけきさしすせそたちつてとなにぬねのはひふへほまみむめもやいゆえよ";
last=''
def rndChar():
    char=chars[random.randint(0, len(chars)-1)]
    if(char!=last):
        return char
    
    return rndChar()

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (0, 0, 0)

width = 15
height = 40
wl=120
hl=60
image = Image.new('RGB', ((width+2)*wl, (height+2)*hl), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype("游明朝体.ttf" ,40)
font1 = ImageFont.truetype("Arial Unicode.ttf", 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)

for i in range(width):
    for j in range(height):
        draw.text((wl * (i+1) , (j+1)*hl), rndChar(), font=font, fill=rndColor2())
# 模糊:
# image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');