import os
import discord
from discord.ext import commands
from datetime import datetime, timezone

TOKEN = open("secret.key").read()

client = commands.Bot(command_prefix=["."])

mememes = client.get_channel(685606448327294990)
isaksightseeing = client.get_channel(811957878448455742)
meet = client.get_channel(702054967808360449)
kod = client.get_channel(758333123338436618)
photoshop = client.get_channel(807232533032599653)
thottierlistt = client.get_channel(830053241915703306)
thotspam = client.get_channel(830765962273488897)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    mememes = client.get_channel(685606448327294990)
    await mememes.send("Dc buttler online. Here to serve!")

@client.command()
async def hej(ctx):
    await ctx.send("Tjo katt")

@client.command()
async def ping(ctx):
    dt = datetime.now(tz=timezone.utc)
    naive = dt.replace(tzinfo=None)
    await ctx.send(f":ping_pong: Bot Latency is {round((naive - ctx.message.created_at).total_seconds() * 1000)}ms. API Latency is {round(client.latency * 1000)}ms")

client.run(TOKEN)