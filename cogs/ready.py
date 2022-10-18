from discord import *
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Setting presence...")
        await self.client.change_presence(activity = Game('Discord Bot by yer#7700'))
        print("Ready!")

# Setup cog...
async def setup(bot):
	await bot.add_cog( Ready(bot) )