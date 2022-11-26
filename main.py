from discord.ext import commands
import os
import discord

intents = discord.Intents.default()


client = commands.Bot(command_prefix="!", intents=intents)

client.load_extension("cogs/test")
client.run(  "MTAzNTU2ODQ2NzQxNzUwMTgxNg.G1Ksnt.Ge8uv2YeZ5W5GVjJQvduTcjuFUVJm9ekUs3YHg")
