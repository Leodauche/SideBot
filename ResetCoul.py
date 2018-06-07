import pickle
ListeCouleur = [
 		('RougeFonce','CC0000') , ('Rouge', 'f44336') , ('Rose', 'e91e63') , ('Violet', '9c27b0') , ('Indigo', '673ab7') , ("BleuFonce", "3f51b5") ,
 		("Bleu", "2196f3") , ("BleuClair", "03a9f4") , ("Cyan", "00bcd4") , ("BleuVert", "009688") , ("Vert", "4caf50") ,
 		("VertClair", "8bc34a") , ("JauneVert", "cddc39") , ("Jaune", "ffff33") , ("Orange", "ff9800") , ("Orange2", "ff5722") , 
 		("Marron", "795548") , ("Blanc", "ffffff") , ("GrisClair", "e0e0e0") , ("Gris", "9e9e9e") , ("GrisFonce", "424242") ,
 		("Noir", "020202") , 
]


f = open('Couleurs.pckl', 'wb')
pickle.dump(ListeCouleur, f)
f.close()