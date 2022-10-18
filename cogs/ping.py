from discord.ext import commands

class Ping(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.command     = "!ping"
		self.description = "Send client latency."
		self.using       = "!ping"

	@commands.command(name="ping", alias=["latency", "bot_latency"])
	async def ping(self, ctx):
		await ctx.send(f"Pong! `{self.client.latency}ms`!")

# Setup cog...
async def setup(bot):
	await bot.add_cog( Ping(bot) )