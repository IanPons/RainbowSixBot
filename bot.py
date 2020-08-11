import discord
from discord.ext import commands
from search_player import buscar_jogador


TOKEN = "MY TOKEN"

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
bot.run(TOKEN)
