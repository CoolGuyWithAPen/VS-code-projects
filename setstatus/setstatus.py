import discord

from redbot.core import commands, app_commands

class SetStatus(commands.Cog):
    """A simple status cog"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(text="The text to set the custom status to")
    async def setstatus(self, interaction: discord.Interaction, text: str):
        """Set a custom status for the bot"""
        if len(text) > 128:
            activity = None
            await interaction.response.send_message("Status must be 128 characters or less.", ephemeral=True)
            return
        else:
            if text == "none":
                activity = None
            else:
                activity = text
        #status = ctx.bot.guilds[0].me.status if len(ctx.bot.guilds) > 0 else discord.Status.online
        #await ctx.bot.change_presence(status=status, activity=activity)
        if activity:
            await interaction.response.send_message(f"Status set to: {activity}", ephemeral=True)
        else:
            await interaction.response.send_message("Custom status cleared.", ephemeral=True)

    @commands.command()
    async def pinging(self, ctx):
        """Funner ping command"""
        # Your code will go here
        await ctx.send("Ponging")