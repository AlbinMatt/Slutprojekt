import discord
from discord.ext import commands

class ssp(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def on_message(message):
        if message.content.startswith('.ssp')
        await ctx.send('Välj sten sax eller påse!')
        ns= await client.wait_for('message' , check=check)






def setup(client):
    client.add_cog(ssp(client))
