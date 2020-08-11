import discord
from discord.ext import commands
from search_player import s_player


TOKEN = "MY TOKEN"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('---- BOT online ----')

@bot.command()
async def StatsPc(ctx, nick):
	await ctx.send(s_player(nick, 'pc'))

@bot.command()
async def StatsPs4(ctx, nick):
	await ctx.send(s_player(nick, 'psn'))

@bot.command()
async def SatsXbox(ctx, nick):
	await ctx.send(s_player(nick, 'xbox'))

'''
bot.run(TOKEN)
