import discord

TOKEN = 'ODUxMTM5MTk0ODUxNDI2MzQ2.YLz7JQ.sJiNqXrzRu190cE0LDFn-HT8Nd8'

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith("!nlp"):
        if client.user != message.author:
            message = message
            await client.send_message(message.channel, message)
            
client.run(TOKEN)
