import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import os
import os.path
import json
import random 

with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)
goldList = os.listdir("./image/goldImage")
on9WaterList = os.listdir("./image/on9Water")

class event(Cog_Extension):
    @Cog_Extension.listener()
    async def on_message(self,message):

        if message.author == self.bot.user:
            return
        if message.author.bot: 
            return

        for i in jdata["goldenText"]:
            if i in message.content:
                image = random.choice(goldList)
                await message.channel.send("咁你有咩高見" , file=discord.File("image/goldImage/" + image))
                return

        for i in jdata["rubbishWater"]:
            if i in message.content:
                image = random.choice(on9WaterList)
                await message.channel.send(file=discord.File("image/on9Water/" + image))
                return

        if "垃圾殺菇咩" in message.content or "垃圾探女" in message.content:
            await message.channel.send(f"{message.author.mention} 55ok")
            return

def setup(bot):
    bot.add_cog(event(bot))