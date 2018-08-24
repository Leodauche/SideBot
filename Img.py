import requests
from PIL import Image, ImageDraw, ImageFont
import random
import string


#Img_list = [ ("image.png" , ([x1,y1],[x1,y1]),size ) , ("image2.png" , ([x1,y1],[x1,y1]),size  ) , .....  ]

Punch_Img_list = [ ("Punch1.png" , ([442,140],[91,50]),100 ) , ("Punch2.jpg" , ([351,6],[135,65]),128 ) , 
					("Punch3.png" , ([200,130],[614,100]),146 ) , ("Punch4.jpg" , ([402,83],[105,69]),80 ) ,
					("Punch5.jpg" , ([700,80],[117,83]),200 ) , ("Punch6.png" , ([372,161],[1177,412]),300 ) ,
					("Punch7.jpg" , ([237,94],[14,16]),100 )  ,("Punch8.jpg" , ([246,54],[529,55]),102 ) , 
					("Punch9.jpg" , ([573,245],[420,16]),130) , ("Punch10.jpg" , ([315,50],[105,63]),42)


				]

def punch_img(url1,url2) :

	taille_liste = len(Punch_Img_list)
	random_img = random.randint(0,taille_liste)-1

	image = Image.open("Donnes/Img/Punch/{}".format(Punch_Img_list[random_img][0]))


	Coord_image_1 = Punch_Img_list[random_img][1][0]

	Coord_image_2 = Punch_Img_list[random_img][1][1]


	Ax1 = Coord_image_1[0]
	Ay1 = Coord_image_1[1]
	Ax2 = Ax1 + Punch_Img_list[random_img][2]
	Ay2 = Ay1 + Punch_Img_list[random_img][2]

	Asize = (Ax2-Ax1,Ay2-Ay1)


	Bx1 = Coord_image_2[0]
	By1 = Coord_image_2[1]
	Bx2 = Bx1 + Punch_Img_list[random_img][2]
	By2 = By1 + Punch_Img_list[random_img][2]

	Bsize = (Bx2-Bx1,By2-By1)



	response1 = requests.get(url1, stream=True)
	response1.raw.decode_content = True
	image1 = Image.open(response1.raw)
	image1.thumbnail(Asize)




	response2 = requests.get(url2, stream=True)
	response2.raw.decode_content = True
	image2 = Image.open(response2.raw)
	image2.thumbnail(Bsize)

	image.paste(image1,(Ax1,Ay1))
	image.paste(image2,(Bx1,By1))


	pathfile = "Donnes/Img/Img_Temp/Punch{}.png".format(id_generator())
	image.save(pathfile, "png")

	return(pathfile)



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
	
