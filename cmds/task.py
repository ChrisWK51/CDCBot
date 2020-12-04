import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import json,asyncio,datetime


class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(783286397632380928)
            while not self.bot.is_closed():
                #await self.channel.send("Hi I'm running!")
                await asyncio.sleep(5)

        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command(name="setchannel")
    async def set_channel(self, ctx , ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"Set Channel: {self.channel.mention}")

    
      
def setup(bot):
    bot.add_cog(Task(bot))