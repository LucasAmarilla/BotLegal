from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, client):
		self.client = client # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		# an example event with cogs
	
	@commands.command()
	async def command(self, ctx):
		# an example command with cogs

def setup(client):
	client.add_cog(Test(client))