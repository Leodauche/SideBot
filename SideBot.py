#SideBot
from PIL import Image, ImageDraw, ImageFont
import discord
import random
import requests
import time
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from Var import Hug , Pat , Rem , Nani , Couleurs
from ImgEdit import img_txt


bot = commands.Bot(command_prefix='!')
emojis = bot.get_all_emojis()
bot.remove_command('help')

@bot.event
async def on_ready():
	print ("SideBot pret")
	await bot.change_presence(game=discord.Game(name='!commandes'))

	
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
	
@bot.command(pass_context=True)
async def pat():
	embed = discord.Embed(color=0xFFC5DF)
	embed.set_image(url="https://cdn.nekos.life/pat/{}.gif".format(random.choice(Pat)))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def hug():
	embed = discord.Embed(color=0xFF1717)
	embed.set_image(url="https://i.imgur.com/{}.gif".format(random.choice(Hug)))
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def kiss(ctx):
	await bot.say(embed=embed)
	await bot.send_file(ctx.message.channel, "Donnes/Img/KissGif/Kiss{}.gif".format(random.randrange(1,13,1)))

	
@bot.command(pass_context=True)
async def rem():
	embed = discord.Embed(color=0x33A8F1)
	embed.set_image(url="https://i.imgur.com/{}".format(random.choice(Rem)))
	await bot.say(embed=embed)
	

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
	msg = await bot.say("Bravo {} , vous avez maintenant le role Rem's Lover ! <:megThumbsup:420974322317000711>".format(ctx.message.author.name))
	await autodestruct(msg,ctx.message,ctx.message.author)

@bot.command(pass_context=True)
async def RemoveRole(ctx,role):
	role = discord.utils.get(ctx.message.server.roles, name=role)
	await bot.remove_roles(ctx.message.author, role)
	

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar de {}".format(user.name), color=0xff0000)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)

	
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

async def autodestruct(msgBot,msgUser,user):
	await bot.add_reaction(msgBot,"👌")
	await bot.wait_for_reaction("👌", message=msgBot, user=user ,timeout=40)
	await bot.delete_message(msgBot)
	await bot.delete_message(msgUser)

bot.run(os.environ.get('BOT_TOKEN'))

