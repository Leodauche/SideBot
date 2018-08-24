from PIL import Image, ImageDraw, ImageFont
import random
import string

#Img_list = [ ("image.png" , [x1,y1,x2,y2] ) , ("image2.png" , [x1,y1,x2,y2] ) , .....  ]

Img_list = [ ("1.png" , [72,60,275,408]) , ("2.png" , [196,232,365,422]) , ("3.png" , [248,400,480,625]) , ("4.jpg" , [75,330,275,572]) , ("5.png" , [150,950,1380,1840]) ,
			("6.jpg" , [110,395,500,640]) , ("7.jpg" , [190,580,640,960]) , ("8.png" , [72,60,275,408]) , ("9.jpg" , [405,160,670,450]) , 
			("10.png" , [140,680,1111,1260]) , ("11.png" , [33,16,272,146]) , ("12.jpg" , [604,304,1318,850]) ]




def img_txt(arg,Texte):
	if arg == "r" :
		taille_liste = len(Img_list)
		random_img = random.randint(0,taille_liste)-1
		img_pathfile = "Donnes/Img/Write/{}".format(Img_list[random_img][0])
		liste_coord = Img_list[random_img][1]

	else : 
		img_pathfile = "Donnes/Img/Write/{}".format(Img_list[int(arg)-1][0]) 
		liste_coord = Img_list[int(arg)-1][1]

	img = Image.open(img_pathfile)

	x1 = liste_coord[0]
	y1 = liste_coord[1]
	x2 = liste_coord[2]
	y2 = liste_coord[3]


	taille_police = 1
	fnt = ImageFont.truetype('Donnes/Fonts/FreeSans.ttf', taille_police)
	size = fnt.getsize(Texte)

	while size[0] < (x2-x1) and size[1] < (y2-y1) :
		taille_police += 1
		fnt = ImageFont.truetype('Donnes/Fonts/FreeSans.ttf', taille_police)
		size = fnt.getsize(Texte)


	taille_police -= 1
	fnt = ImageFont.truetype('Donnes/Fonts/FreeSans.ttf', taille_police)
	size = fnt.getsize(Texte)



	d = ImageDraw.Draw(img)
	x_offset = x1+(x2-x1)/2-(size[0])/2
	y_offset = y1+(y2-y1)/2-(size[1])/2
	d.text((x_offset,y_offset),  Texte ,font=fnt, fill = (0,0,0,255) )

	box = (x1,y1,x2,y2)

	pathfile = "Donnes/Img/Img_Temp/Img_Edit{}.png".format(id_generator())
	img.save(pathfile, "png")
	return(pathfile)



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
