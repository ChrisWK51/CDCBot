import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import json

with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)

class cmdErrorHandler(Cog_Extension):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            index = jdata["Command"].index(ctx.command.name)
            await ctx.reply(jdata["CommandError"][index])
        except Exception:
            print(error)
            await ctx.reply("冇呢個指令啊 等下啦")

def setup(bot):
    bot.add_cog(cmdErrorHandler(bot))