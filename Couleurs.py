from PIL import Image, ImageDraw, ImageFont
import random
import string
import pickle


f = open('Couleurs.pckl', 'rb')
ListeCouleur = pickle.load(f)
f.close()

def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def afficherCouleur() :
	nbrLignes = round(len(ListeCouleur)/3+0.4)
	#print(nbrLignes)
	Img = Image.new('RGBA', (900,nbrLignes*40), color = (0,0,0,0))
	colone = 0
	for i in range (len(ListeCouleur)) :
		ligne = i-nbrLignes*colone
		if ligne >= nbrLignes :
			colone += 1
			ligne = 0
		fnt = ImageFont.truetype('Donnes/Fonts/FreeSans.ttf', 30)
		Couleur = ListeCouleur[i]
		size = fnt.getsize(Couleur[0])
		carre_image = Image.new('RGB',(60,30), color =hex_to_rgb(Couleur[1]))
		texte = Image.new('RGBA', ((size[0]+5),(size[1]+5)), color = (0,0,0,0))
		d = ImageDraw.Draw(texte)
		d.text((5,5), Couleur[0] ,font=fnt , fill=hex_to_rgb(Couleur[1]))
		Img.paste(carre_image,(colone*295+5,ligne*40+5))
		Img.paste(texte,(colone*295+70,ligne*40))
		i += 1


	pathfile = "Donnes/Img/Img_Temp/CoulCache{}.png".format(id_generator())
	Img.save(pathfile, "png")
	return(pathfile)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))