# -*- coding: utf-8 -*-
import Image, ImageDraw, ImageFont

def drawNum(num,avatar,location):
	"""
	对输入的头像图片，再其右上角写入红色数字标记
	
	"""
	im = Image.open(avatar)

	position = (im.size[0]-im.size[1]/10,0)
	imFormat = im.format
	print im.mode
	font = ImageFont.truetype("Arial.ttf",36)
	
	draw = ImageDraw.Draw(im)

	draw.text(position,num,fill="#ff0000",font=font)
       
	im.save(location,imFormat)




if __name__ == "__main__":

	import os, sys
	BASE_DIR = os.path.dirname(os.path.abspath( sys.argv[0] ))

	imageDIR = os.path.abspath(os.path.join(BASE_DIR,"sample"))

	sys.argv=[sys.argv[0],"3","1.jpeg","1_result.jpeg"]

	drawNum(sys.argv[1],os.path.join(imageDIR,sys.argv[2]),os.path.join(imageDIR,sys.argv[3]))
	sys.argv=[sys.argv[0],"9","2.png","2_result.png"]
	drawNum(sys.argv[1],os.path.join(imageDIR,sys.argv[2]),os.path.join(imageDIR,sys.argv[3]))


