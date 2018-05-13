from PIL import Image, ImageDraw, ImageFont
import random
import string

def img_txt(Texte):
	img = Image.open('Donnes/Img/Img_Edit.png')

	x1 = 72
	y1 = 60
	x2 = 275
	y2 = 408
	taille_police = 60
	max_charPerLine = round((x2-x1)/32,0)
	print(max_charPerLine)
	print("ou sinon1 ", int((x2-x1)/32))

	txt = Image.new('RGB', (x2-x1, y2-y1), color = (255, 255, 255))
	fnt = ImageFont.truetype('Donnes/Fonts/FreeSans.ttf', taille_police)
	size = fnt.getsize(Texte)
	print(size)
	if (len(Texte) > max_charPerLine) :
		nbr_element_liste = round((len(Texte)/max_charPerLine),0)
		print("ou sinon ", int(len(Texte)/max_charPerLine))
		print("couper le Texte en : ",nbr_element_liste)

	d = ImageDraw.Draw(txt)
	x_offset = (x2-x1)/2-(size[0])/2
	y_offset = (y2-y1)/2-(size[1])/2
	d.text((x_offset,y_offset), Texte ,font=fnt , fill=(0,0,0))

	box = (x1,y1,x2,y2)
	img.paste(txt,(x1,y1))

	pathfile = "Donnes/Img/Img_Temp/Img_Edit{}.png".format(id_generator())
	img.save(pathfile, "png")
	return(pathfile)



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
