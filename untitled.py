from PIL import Image, ImageDraw, ImageFont
import random
import string

ListeCouleur = [

		("RougeFonce","CC0000") , ("Rouge", "f44336") , ("Rose", "e91e63") , ("Violet", "9c27b0") , ("Indigo", "673ab7") , ("BleuFonce", "3f51b5") ,
		("Bleu", "2196f3") , ("BleuClair", "03a9f4") , ("Cyan", "00bcd4") , ("BleuVert", "009688") , ("Vert", "4caf50") ,
		("VertClair", "8bc34a") , ("JauneVert", "cddc39") , ("Jaune", "ffff33") , ("Orange", "ff9800") , ("Orange2", "ff5722") , 
		("Marron", "795548") , ("Blanc", "ffffff") , ("GrisClair", "e0e0e0") , ("Gris", "9e9e9e") , ("GrisFonce", "424242") ,
		("Noir", "000000") , 
]

def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def afficherCouleur() :
	nbrLignes = round(len(ListeCouleur)/3+0.4)
	print(nbrLignes)
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


	pathfile = "Donnes/Img/ImgEditCache/CoulCache{}.png".format(id_generator())
	Img.save(pathfile, "png")
	return(pathfile)
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
print(afficherCouleur())