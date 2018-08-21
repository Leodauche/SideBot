#SideBot
from PIL import Image, ImageDraw, ImageFont
import discord
import random
import aiohttp
import time
import os
import asyncio
import pickle
from discord.ext import commands
from discord.ext.commands import Bot
from Var import Hug , Pat ,Nani
from Couleurs import afficherCouleur , ListeCouleur
from ImgEdit import img_txt, Img_list
import Couleurs


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print ("SideBot pret")
	await bot.change_presence(game=discord.Game(name='!commandes'))











async def comReac(ctx,user,msg,page,nbrPages):
	reac_msg = await bot.wait_for_reaction(['⏪', '◀','▶','⏩','❌'],user=user, message=msg)

	if (reac_msg.reaction.emoji == '⏪') :
		page = 1
		print("page = ",page)

	if (reac_msg.reaction.emoji == '◀') :
		if(page > 1) :
			page = page-1
			print("page = ",page)

	if (reac_msg.reaction.emoji == '▶') :
		if (page < nbrPages) :
			page = page+1
			print("page = ",page)

	if (reac_msg.reaction.emoji == '⏩') :
		page = nbrPages
		print("page = ",page)

	if (reac_msg.reaction.emoji == '❌') :
		page = 0
		await bot.delete_message(msg)
		await bot.delete_message(ctx.message)

	return int(page)






	
@bot.command(pass_context=True)
async def commandes(ctx):
	page:int = 1
	nbrPages:int = 3

	embed1=discord.Embed(title="Commandes d'images :", description="---------------------------------------------------------", color=0x55aafe)
	embed1.set_author(name="Commandes de SideBot")
	embed1.set_thumbnail(url=bot.user.avatar_url)
	embed1.add_field(name="safeb", value="Permet d'envoyer x images avec y tag depuis safebooru, c'écrit sous la forme `!safeb x y`", inline=True)
	embed1.add_field(name="rem", value="Envoie une image de Rem", inline=False)
	embed1.add_field(name="batman", value="Envoie une image de Batman", inline=False)
	embed1.add_field(name="kiss", value="Envoie un baiser", inline=False)
	embed1.add_field(name="hug", value="Envoie un câlin", inline=False)
	embed1.add_field(name="pat", value="Envoie une caresse", inline=False)
	embed1.add_field(name="nani", value="NANI", inline=False)
	embed1.add_field(name="chat", value="Envoie un chat :3", inline=False)
	embed1.add_field(name="neko", value="Envoie une neko :3", inline=False)
	embed1.set_footer(text="bot pas codé par Kinji, page {} / {}".format(page,nbrPages))


	embed2=discord.Embed(title="Commandes d'images :", description="---------------------------------------------------------", color=0x55aafe)
	embed2.set_author(name="Commandes de SideBot")
	embed2.set_thumbnail(url=bot.user.avatar_url)
	embed2.set_footer(text="bot pas codé par Kinji, page {} / {}".format(page,nbrPages))



	embed3=discord.Embed(title="Commandes d'images :", description="---------------------------------------------------------", color=0x55aafe)
	embed3.set_author(name="Commandes de SideBot")
	embed3.set_thumbnail(url=bot.user.avatar_url)
	embed3.set_footer(text="bot pas codé par Kinji, page {} / {}".format(page,nbrPages))


	msg = await bot.say(embed=embed1)

	await bot.add_reaction(msg,"⏪")
	await bot.add_reaction(msg,"◀")
	await bot.add_reaction(msg,"▶")
	await bot.add_reaction(msg,"⏩")
	await bot.add_reaction(msg,"❌")

	while True :

		page = await comReac(ctx,ctx.message.author,msg,page,nbrPages)

		if page == 0 :
			break 
	
		if page == 1 :
			await bot.edit_message(msg,embed=embed1)

		if page == 2 :
			await bot.edit_message(msg,embed=embed2)

		if page == 3 :
			await bot.edit_message(msg,embed=embed3)








@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("Pong ! 🏓")


@bot.command(pass_context=True)
async def wait(ctx,nombre):
	await bot.say("début")
	time.sleep(int(nombre))
	await bot.say("fin")



@bot.command(pass_context=True)
async def write(ctx,arg,*, Texte=None):
	if arg == "help" :
		await bot.say("aled")
	elif arg == "r" :
		pathfile = img_txt(arg,Texte)
		await bot.send_file(ctx.message.channel,pathfile)
		os.remove(pathfile)
	else : 
		try : 
			int(arg)
		except ValueError:
			await bot.say("erreur dans la commande")
	if int(arg) > 0 and int(arg) < len(Img_list)+1 :
		pathfile = img_txt(arg,Texte)
		await bot.send_file(ctx.message.channel,pathfile)
		os.remove(pathfile)
	else:
		await bot.say("nombre trop grand ou trop petit")



@bot.command(pass_context=True)
async def delete(ctx, nombre):
	admin = discord.utils.get(ctx.message.server.roles, id='416319027191873538')
	modo = discord.utils.get(ctx.message.server.roles, id='420960024437719050')
	if (ctx.message.author.top_role == admin) or (ctx.message.author.top_role == modo) :
		await bot.purge_from(ctx.message.channel, limit=int(nombre))
	else :
		msg = await bot.say("Vous ne pouvez pas utiliser cette commande")
		await autodestruct(msg,ctx.message,ctx.message.author)


@bot.command(pass_context=True)
async def safeb(ctx,limit,*,tags):
	if int(limit) >= 5 :
		await bot.say("calmos amigos")
	else :
		tags_joined = tags.replace(" ","+")
		async with aiohttp.ClientSession() as session:
			async with session.get('https://safebooru.org//index.php?page=dapi&tags={}&s=post&limit={}&q=index&json=1'.format(tags_joined,limit)) as r: 
				js = await r.json(content_type='text/html')
				for i in range(len(js)):
					arr = js[i]
					await bot.say("https://safebooru.org//images/{}/{}".format(arr['directory'],arr['image']))

@bot.command(pass_context=True)
async def batman(ctx):
	fp = "Donnes/Img/Batman/{}".format(random.choice(os.listdir("Donnes/Img/Batman")))
	await bot.send_file(ctx.message.channel, fp )
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def nani():
	embed = discord.Embed(color=0x6D1717)
	embed.set_image(url="https://imgur.com/{}".format(random.choice(Nani)))
	await bot.say(embed=embed)
	await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
async def pat():
	embed = discord.Embed(color=0xFFC5DF)
	embed.set_image(url="https://cdn.nekos.life/pat/{}.gif".format(random.choice(Pat)))
	await bot.say(embed=embed)
	await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
async def hug():
	embed = discord.Embed(color=0xFF1717)
	embed.set_image(url="https://i.imgur.com/{}.gif".format(random.choice(Hug)))
	await bot.say(embed=embed)
	await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def kiss(ctx):
	fp = "Donnes/Img/KissGif/{}".format(random.choice(os.listdir("Donnes/Img/KissGif")))
	await bot.send_file(ctx.message.channel, fp)
	await bot.delete_message(ctx.message)

	
@bot.command(pass_context=True)
async def rem(ctx):
	fp = "Donnes/Img/Rem/{}".format(random.choice(os.listdir("Donnes/Img/Rem")))
	await bot.send_file(ctx.message.channel, fp )
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def say(ctx,*,message):
	await bot.say(str(message))

@bot.command(pass_context=True)
async def sayd(ctx,*,message):
	await bot.say(str(message))
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def vote(ctx, vote_type:int=None ,Vote_Message=None, emoji1 = "👍", emoji2 = "👎"):
	admin = discord.utils.get(ctx.message.server.roles, id='416319027191873538')
	modo = discord.utils.get(ctx.message.server.roles, id='420960024437719050')
	siders = discord.utils.get(ctx.message.server.roles, id='416319131361476629')
	print("vote_type : ",vote_type)
	print("Vote_Message : ",Vote_Message)
	print("emoji1 : ",emoji1)
	print("emoji2: ",emoji2)
	if (ctx.message.author.top_role == admin) or (ctx.message.author.top_role == modo) or (ctx.message.author.top_role == modo) :
		if(vote_type==1):
			Vote_Msg_Env = await bot.say(str(Vote_Message))
			await bot.add_reaction(Vote_Msg_Env, emoji1)
			await bot.add_reaction(Vote_Msg_Env, emoji2)
		else:
			msg = await bot.say("Aide pour la comande")
			await autodestruct(msg,ctx.message,ctx.message.author)
	else :
		msg = await bot.say("Vous n'avez pas la permission d'utiliser cette commande")
		await autodestruct(msg,ctx.message,ctx.message.author)

@bot.command(pass_context=True)
async def rp(ctx,arg):
	role = discord.utils.get(ctx.message.server.roles, name='rp')
	if arg == "join":
		await bot.add_roles(ctx.message.author, role)
		msg = await bot.say("{}, vous avez maintenant acces au channel #rp ".format(ctx.message.author.name))
		await autodestruct(msg,ctx.message,ctx.message.author)

	elif arg == "leave":
		await bot.remove_roles(ctx.message.author, role)
		msg = await bot.say("{}, vous avez bien quité le channel #rp ".format(ctx.message.author.name))
		await autodestruct(msg,ctx.message,ctx.message.author)

	elif arg == "help":
		embed=discord.Embed(title="Aide de la commande `!rp`", description="----------------------------------------------------------------------------", color=0x389c43)
		embed.add_field(name="La commande `!rp` permet d’accéder au channel #rp", value="utilisation :", inline=False)
		embed.add_field(name="!rp help", value="permet d'afficher l'aide", inline=False)
		embed.add_field(name="!rp join", value="permet de rejoindre le channel #rp", inline=False)
		embed.add_field(name="!rp leave", value="permet de quitter le channel #rp", inline=False)
		await bot.say(embed=embed)


	else :
		await bot.say("Vous avez fait une erreur dans la commande faites `!rp help` pour afficher l'aide")
		await autodestruct(msg,ctx.message,ctx.message.author)





@bot.command(pass_context=True)
async def loveRem(ctx):
	role = discord.utils.get(ctx.message.server.roles, id='418870888906227712')
	await bot.add_roles(ctx.message.author, role)
	msg = await bot.say("Bravo {} , vous avez maintenant le role Rem's Lover ! <:megThumbsup:439481053820878878>".format(ctx.message.author.name))
	await autodestruct(msg,ctx.message,ctx.message.author)


@bot.command(pass_context=True)
async def emoji(ctx, emoji: discord.Emoji):
	embed = discord.Embed(color=0x4286f4)
	embed.set_image(url=emoji.url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar de {}".format(user.name), color=0xff0000)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def Say3(ctx,Texte):
	Chnl = bot.get_channel("447763181314768896")
	await bot.send_message(Chnl,str(Texte))

@bot.command(pass_context=True)
async def creerRoles(ctx):

	Roles_Serv = ctx.message.server.roles
	Tuple_Roles_Serv = []
	ListeCouleur2 = list(ListeCouleur)

	for i in range (len(Roles_Serv)) :
		HexRole = str(Roles_Serv[i].colour)
		Tuple = tuple([Roles_Serv[i].name,HexRole.replace("#","")])
		Tuple_Roles_Serv.append(Tuple)

	for i in range (len(ListeCouleur)-1,-1,-1):
		RoleCouleur = ListeCouleur[i]

		for j in range (len(Tuple_Roles_Serv)):
			Role_Serv = Tuple_Roles_Serv[j]

			if RoleCouleur[0] == Role_Serv[0] :
				try : 
					ListeCouleur2.pop(i)
				except(IndexError) :
					break

				if RoleCouleur[1] != Role_Serv[1] :
					Role_Edit = discord.utils.get(ctx.message.server.roles, id=Roles_Serv[j].id)
					await bot.edit_role(server = ctx.message.server,role=Role_Edit,colour = discord.Colour(int(RoleCouleur[1], 16)))

	for i in range (len(ListeCouleur2)):
		Role = ListeCouleur2[i]
		await bot.create_role(server = ctx.message.server, name=Role[0],colour=discord.Colour(int(Role[1], 16)))


@bot.command(pass_context=True)
async def affCoul(ctx):
	admin = discord.utils.get(ctx.message.server.roles, id='416319027191873538')
	if ctx.message.author.top_role == admin :
		pathfile = afficherCouleur()
		await bot.send_file(ctx.message.channel,pathfile)
		os.remove(pathfile)
	else :
		msg = await bot.say("Vous ne pouvez pas utiliser cette commande")
		await autodestruct(msg,ctx.message,ctx.message.author)


@bot.command(pass_context=True)
async def Couleur(ctx,Couleur):

	Roles_Serv = ctx.message.server.roles
	CoulDispo = []
	Noms_Roles = []

	for i in range (len(Roles_Serv)) : 
		Noms_Roles.append(Roles_Serv[i].name)

	for i in range (len(ListeCouleur)) :
		RoleCouleurTest = ListeCouleur[i]

		for j in range (len(Noms_Roles)):
			Role_Serv_Test = Noms_Roles[j]

			if Role_Serv_Test == RoleCouleurTest[0] :
				CoulDispo.append(Role_Serv_Test)


	Roles_User = ctx.message.author.roles
	Noms_Roles_User = []

	for i in range (len(Roles_User)) :
		Noms_Roles_User.append(Roles_User[i].name)
	Roles_User_Couleur = list(set(Noms_Roles_User).intersection(CoulDispo))
	#print("Roles_User_Couleur = ", Roles_User_Couleur)

	if Roles_User_Couleur == [] :
		if str(Couleur) in CoulDispo :
			role = discord.utils.get(ctx.message.server.roles, name=Couleur)
			await bot.add_roles(ctx.message.author, role)
		else :
			print("la couleur n'existe pas")

	else :
		if str(Couleur) in CoulDispo :
			if str(Couleur) in Roles_User_Couleur :
				print("vous avez deja cette couleur")
				print("Supprimer tt les autres couleurs")
			else :
				for i in range (len(Roles_User_Couleur)):
					#print("len role user couleur = ",len(Roles_User_Couleur))
					#print("i = ",i)
					roleDel = discord.utils.get(ctx.message.server.roles, name=Roles_User_Couleur[i])
					await bot.remove_roles(ctx.message.author, roleDel)
					await asyncio.sleep(1)
					#print("Role del : ", roleDel)
				roleAdd = discord.utils.get(ctx.message.server.roles, name=Couleur)
				await bot.add_roles(ctx.message.author, roleAdd)
		else :
			print("la couleur n'existe pas")
	

@bot.command(pass_context=True)
async def AddColor(ctx, NomCouleur,HexCouleur, Position):
	Coultuple = (NomCouleur,HexCouleur)
	ListeCouleur.insert(int(Position), Coultuple)
	msg = await bot.say("La couleur {} , {} , a bien été ajoutée au rang {}".format(NomCouleur,HexCouleur,int(Position)))
	await Save_ListeCouleur(ListeCouleur)
	await autodestruct(msg,ctx.message,ctx.message.author)
	
@bot.command(pass_context=True)
async def RemoveColor(ctx,Position):
	msg1 = await bot.say("Voulez vous enlever la couleur {} ?".format(ListeCouleur[int(Position)]))
	await bot.add_reaction(msg1,"👍")
	await bot.add_reaction(msg1,"👎")
	reac_msg1 = await bot.wait_for_reaction(['👍', '👎'],user=ctx.message.author, message=msg1)

	if(reac_msg1.reaction.emoji == '👍'):
		msga1 = await bot.say("La couleur {} a bien été supprimée".format(ListeCouleur[int(Position)]))
		ListeCouleur.pop(int(Position))
		await Save_ListeCouleur(ListeCouleur)

	elif(reac_msg1.reaction.emoji == '👎'):
		msgb1 = await bot.say("Voulez-vous supprimer une autre couleur ?")
		await bot.add_reaction(msgb1,"👍")
		await bot.add_reaction(msgb1,"👎")
		reac_msgb1 = await bot.wait_for_reaction(['👍', '👎'],user=ctx.message.author, message=msgb1)

		if(reac_msgb1.reaction.emoji == '👍'):
			await bot.say("dzdqsd")
		elif(reac_msgb1.reaction.emoji == '👎'):
			await bot.say("aaaadzdqsd")


@bot.command(pass_context=True)
async def chat(ctx):
	async with aiohttp.ClientSession() as session:
		async with session.get('http://aws.random.cat/meow') as r: 
			if r.status == 200 :
				js = await r.json()
				await bot.send_message(ctx.message.channel, js['file'])

@bot.command(pass_context=True)
async def neko(ctx):
	async with aiohttp.ClientSession() as session:
		async with session.get('https://nekos.life/api/v2/img/neko') as r: 
			if r.status == 200 :
				js = await r.json()
				await bot.send_message(ctx.message.channel, js['url'])

@bot.command(pass_context=True)
async def infos(ctx, user: discord.Member):
    embed = discord.Embed(title="Info sur {}".format(user.name), color=0x00ff00)
    embed.add_field(name="Nom", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Statut", value=user.status, inline=True)
    embed.add_field(name="Plus haut role", value=user.top_role)
    embed.add_field(name="arrivé(e) le", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

async def Save_ListeCouleur (ListeCouleur):
	f = open('Couleurs.pckl', 'wb')
	pickle.dump(ListeCouleur, f)
	f.close()



async def autodestruct(msgBot,msgUser,user):
	await bot.add_reaction(msgBot,"❌")
	await bot.wait_for_reaction("❌", message=msgBot, user=user ,timeout=40)
	await bot.delete_message(msgBot)
	await bot.delete_message(msgUser)

#bot.run(os.environ.get('BOT_TOKEN'))
bot.run("NDE2MzIxMzI0ODczNjc4ODU4.Dl2iUg.4z4LnVUPJXxeuKLey4AgdcUTepQ")
