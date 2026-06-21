import discord

from redbot.core import commands, app_commands

class Status(commands.Cog):
    """A simple status cog"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(status="The text to set the custom status to")
    async def setstatus(self, ctx, interaction: discord.Interaction, status: str):
        """Set a custom status for the bot"""
        if len(status) > 128:
            activity = None
            await interaction.response.send_message("Status must be 128 characters or less.", ephemeral=True)
            return
        else:
            if status:
                activity = status
            else:
                activity = None
        await ctx.bot.change_presence(status="online", activity=activity)
        await interaction.response.send_message(f"Status set to: {status}", ephemeral=True)

    @commands.command()
    async def pinging(self, ctx):
        """Funner ping command"""
        # Your code will go here
        await ctx.send("Ponging")
