import discord
from discord.ext import commands
from search_player import buscar_jogador


TOKEN = "Njk3NTA3ODgzOTQ4MDQ4NDQ0.Xo5SbA.Rbqf3ClzD9X9_emsRslf_oOzzRg"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('---- BOT online ----')

@bot.command()
async def StatsPc(ctx, nick):
	await ctx.send(buscar_jogador(nick, 'pc'))

@bot.command()
async def StatsPs4(ctx, nick):
	await ctx.send(buscar_jogador(nick, 'psn'))

@bot.command()
async def SatsXbox(ctx, nick):
	await ctx.send(buscar_jogador(nick, 'xbox'))



'''
@bot.command()
async def DanielDeKaid(ctx):
	await ctx.send('D E R R O T A')

@bot.command()
async def PedroDeDoc(ctx):
	await ctx.send('C O R R E')

@bot.command()
async def Jotape1(ctx):
	await ctx.send('Planet Time')

@bot.command()
async def Jotape2(ctx):
	await ctx.send('Fake Alibi')


@bot.command()
async def Lucas(ctx):
	await ctx.send('Mr.1v1')

'''
bot.run(TOKEN)
