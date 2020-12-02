import discord
from discord.ext import commands
from  core.classes import Cog_Extension


class Main(Cog_Extension):
    @commands.command()
    async def ping(self , ctx):
        await ctx.send(f"殺菇咩連地球既ping數係 : {round(self.bot.latency * 10)} ms")
    
def setup(bot):
    bot.add_cog(Main(bot))