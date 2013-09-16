#!/usr/bin/python

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.new("RGB",(1280,720),"#000")
draw = ImageDraw.Draw(im)

x,y = im.size

fontPosition=(10,360)

font = ImageFont.truetype('helvetica_neue_lt.ttf',60)
draw.text(fontPosition,'ROBERT NEDERHORST',font=font, fill='#333')

mask = Image.new("L",im.size,color=0)
drawAlpha = ImageDraw.Draw(mask)
drawAlpha.text(fontPosition,'test stuff here',font=font, fill='#fff')

im.putalpha(mask)
im.save('foo.png','PNG')

