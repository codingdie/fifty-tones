# -*- coding: utf-8 -*-  

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母:
pingjia=u"あいうえおかきくけきさしすせそたちつてとなにぬねのはひふへほまみむめもやいゆえよらりるれろわいうえを";
pianjia=u"アイウエオカキクケコサィシセソタチツテトナニヌネノハヒフヘホマミムメモヤイユエヨラリルレロワイウエヲ";
last=''
def rndChar(chars):
    char=chars[random.randint(0, len(pingjia)-1)]
    if(char!=last):
        return char
    return rndChar()

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


width = 15
height = 20
wl=120
hl=130

def generate(file,chars):
    image = Image.new('RGB', ((width+2)*wl, (height+1)*hl), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype("游明朝体.ttf" ,50)
    # font1 = ImageFont.truetype("Arial Unicode.ttf", 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    for i in range(width):
        for j in range(height):
            draw.text((wl * (i+1) , (j+1)*hl), rndChar(chars), font=font, fill= (0, 0, 0))
    # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    image.save(file, 'jpeg');

generate('pingjia.jpg',pianjia);
generate('pianjia.jpg',pianjia);
