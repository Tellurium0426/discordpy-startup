from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('Fortnite'))

@bot.command()
async def fuck(ctx):
    await ctx.send('pong')

bot.run(token)
