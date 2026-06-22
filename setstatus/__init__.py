from .setstatus import SetStatus


async def setup(bot):
    await bot.add_cog(SetStatus(bot))