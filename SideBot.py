#SideBot
from PIL import Image, ImageDraw, ImageFont
import discord
import random
import requests
import time
import os
import asyncio
import pickle
from discord.ext import commands
from discord.ext.commands import Bot
from Var import Hug , Pat ,Nani
from Couleurs import afficherCouleur , ListeCouleur
from ImgEdit import img_txt
import Couleurs


bot = commands.Bot(command_prefix='!')
emojis = bot.get_all_emojis()
bot.remove_command('help')

@bot.event
async def on_ready():
	print ("SideBot pret")
	await bot.change_presence(game=discord.Game(name='!commandes'))
	#print (ListeCouleur)

	
@bot.command(pass_context=True)
async def commandes():
	embed = discord.Embed(title="Commandes de SideBot", color=0x800000)
	embed.add_field(name="nani", value="NANI????", inline=False)
	embed.add_field(name="ping", value="dit pong", inline=False)
	embed.add_field(name="rem", value="Envoie une image de la meilleure waifu", inline=False)
	embed.add_field(name="avatar", value="Donne l'avatar d'un utilisateur", inline=False)
	embed.add_field(name="infos", value="Donne des informations sur un utilisateur", inline=False)
	msg = await bot.say(embed=embed)
	await autodestruct(msg,ctx.message,ctx.message.author)

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("Pong ! 🏓")


@bot.command(pass_context=True)
async def wait(ctx,nombre):
	await bot.say("début")
	time.sleep(int(nombre))
	await bot.say("fin")



@bot.command(pass_context=True)
async def test(ctx, Texte):
	pathfile = img_txt(Texte)
	await bot.send_file(ctx.message.channel,pathfile)
	os.remove(pathfile)


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
	await bot.delete_message(ctx.messager)
	
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






"""
@bot.command(pass_context=True)
async def couleur(ctx, arg1, arg2=None):
	Arg1=str(arg1)
	if(Arg1.lower()=="reset"):
		roles = ctx.message.author.roles
		print(roles)
		print(len(roles))
		for i in range(0,len(roles)):
			nomRoles = roles[i].name
			print("nom role = ", nomRoles)
			if (nomRoles in Couleurs):
				nomRolesId = discord.utils.get(ctx.message.server.roles, name=nomRoles)
				await bot.remove_roles(ctx.message.author, nomRolesId)
				print(nomRoles,"enlevé")
			i += 1
			print(i)
			time.sleep(0.5)
		msg = await bot.say("Votre couleur a bien été enlevée, si ce n'est pas le cas contacter un adminitrateur pour qu'il vous le fasse manuellement")
		await autodestruct(msg,ctx.message,ctx.message.author)
	elif(Arg1.lower()=="help"):
		CoulEmb = discord.Embed(title="La commande !couleur vous permet de changer la couleur de votre pseudo sur le serveur", color=0x0a00ff)
		CoulEmb.set_author(name="Guide de la commande !couleur")
		CoulEmb.add_field(name="Pour ajouter une couleur faites :", value="```!couleur + nomDeLaCouleur```", inline=False)
		CoulEmb.add_field(name="Pour enlever une couleur faites :", value="```!couleur - nomDeLaCouleur```", inline=False)
		CoulEmb.add_field(name="Pour réinisialliser vos couleurs faites :", value="```!couleur reset```", inline=False)
		CoulEmb.add_field(name="Voici les couleurs disponibles :", value=Couleurs, inline=False )
		msg = await bot.say(embed=CoulEmb)
		await autodestruct(msg,ctx.message,ctx.message.author)
	elif(Arg1=="+"):
		Couleur=str(arg2)
		if(Couleur in Couleur):
			role = discord.utils.get(ctx.message.server.roles, name=Couleur.lower())
			await bot.add_roles(ctx.message.author, role)
		else:
			msg = await bot.say("La couleur que vous voulez n'éxiste pas, pour voir les couleurs disponibles faites ```!couleur help```")
			await autodestruct(msg,ctx.message,ctx.message.author)
	elif(Arg1=="-"):
		Couleur=str(arg2)
		if(Couleur in Couleur):
			role = discord.utils.get(ctx.message.server.roles, name=Couleur.lower())
			await bot.remove_roles(ctx.message.author, role)
		else:
			msg = await bot.say("La couleur que vous voulez n'éxiste pas, pour voir les couleurs disponibles faites ```!couleur help```")
			await autodestruct(msg,ctx.message,ctx.message.author)
	else:
		msg = await bot.say("Vous vous etes trompé dans la commande, pour voir comment s'en servir faites : ```!couleur help```")
		await autodestruct(msg,ctx.message,ctx.message.author)
"""		


@bot.command(pass_context=True)
async def loveRem(ctx):
	role = discord.utils.get(ctx.message.server.roles, id='418870888906227712')
	await bot.add_roles(ctx.message.author, role)
	msg = await bot.say("Bravo {} , vous avez maintenant le role Rem's Lover ! <:megThumbsup:439481053820878878>".format(ctx.message.author.name))
	await autodestruct(msg,ctx.message,ctx.message.author)


@bot.command(pass_context=True)
async def emoji(ctx, emoji: discord.Emoji):
	#embed = discord.Embed(title = ":{}:".format(emoji.name),color=0x4286f4)
	embed = discord.Embed(color=0x4286f4)
	embed.set_image(url=emoji.url)
	await bot.say(embed=embed)

"""
@bot.command(pass_context=True)
async def RemoveRole(ctx,role):
	role = discord.utils.get(ctx.message.server.roles, name=role)
	await bot.remove_roles(ctx.message.author, role)
	
"""
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
		await bot.send_file(ctx.message.channel,afficherCouleur())
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
	print("Roles_User_Couleur = ", Roles_User_Couleur)

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
					print("len role user couleur = ",len(Roles_User_Couleur))
					print("i = ",i)
					roleDel = discord.utils.get(ctx.message.server.roles, name=Roles_User_Couleur[i])
					await bot.remove_roles(ctx.message.author, roleDel)
					await asyncio.sleep(1)
					print("Role del : ", roleDel)
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
async def infos(ctx, user: discord.Member):
    embed = discord.Embed(title="Info sur {}".format(user.name), color=0x00ff00)
    embed.add_field(name="Nom", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Statut", value=user.status, inline=True)
    embed.add_field(name="Plus haut role", value=user.top_role)
    embed.add_field(name="arrivé(e) le", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
"""
@bot.command(pass_context=True)
async def test2(ctx,nomRole,couleur):
	await bot.create_role(server = ctx.message.server, name=nomRole,colour=discord.Colour(int(couleur, 16)))
	msg = await bot.say("le role {} a bien été créé".format(nomRole))
	await autodestruct(msg,ctx.message,ctx.message.author)
"""
async def Save_ListeCouleur (ListeCouleur):
	f = open('Couleurs.pckl', 'wb')
	pickle.dump(ListeCouleur, f)
	f.close()



async def autodestruct(msgBot,msgUser,user):
	await bot.add_reaction(msgBot,"👌")
	await bot.wait_for_reaction("👌", message=msgBot, user=user ,timeout=40)
	await bot.delete_message(msgBot)
	await bot.delete_message(msgUser)

bot.run(os.environ.get('BOT_TOKEN'))

