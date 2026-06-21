import discord

from redbot.core import commands, app_commands

class Status(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!", ephemeral=True)

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
