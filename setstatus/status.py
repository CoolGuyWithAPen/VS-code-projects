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
            if status == "none":
                activity = None
            else:
                activity = status
        online = ctx.bot.guilds[0].me.status if len(ctx.bot.guilds) > 0 else discord.Status.online
        await ctx.bot.change_presence(status=online, activity=activity)
        if activity:
            await ctx.send(_("Custom status set to `{activity}`.").format(activity=activity))
        else:
            await ctx.send(_("Custom status cleared."))
        #await interaction.response.send_message(f"Status set to: {activity}", ephemeral=True)

    @commands.command()
    async def pinging(self, ctx):
        """Funner ping command"""
        # Your code will go here
        await ctx.send("Ponging")
