import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import os
import os.path
import json
import random 
from discord.utils import get

with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)
goldList = os.listdir("./image/goldImage")
on9WaterList = os.listdir("./image/on9Water")

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("Hello")
        channel = self.bot.get_channel(int(jdata['Welcome_Channel']))
        await channel.send(f"{member.mention} 入左黎 ! ")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("Hello")
        channel = self.bot.get_channel(int(jdata['Leave_Channel']))
        await channel.send(f"{member.name} 走左佬 !")

            
    @commands.Cog.listener()
    async def on_message(self,message):

        if message.author == self.bot.user:
            return
        if message.author.bot: 
            return

        if message.author == self.bot.get_user(int(jdata['redTeaId'])):
            await message.reply(f"https://embassies.gov.il/hong-kong/Pages/default.aspx\nhttps://www.gov.uk/world/organisations/british-consulate-general-hong-kong" )


        if message.content == "<:20200925124257:759096369985224706>" and message.author == self.bot.get_user(174912315278229504) :
            await message.reply(f"<:20200925124257:759096369985224706>")
        
        for i in jdata["goldenText"]:  #當段野 有"咁你" "錦鯉"etc 會  trigger 
            if i in message.content:
                image = random.choice(goldList)
                await message.reply("咁你有咩高見" , file=discord.File("image/goldImage/" + image))
                
        if message.content in jdata["rubbishWater"]:    #當段野 剩係得"鈴狗""鈴緒on9"會  trigger 
            image = random.choice(on9WaterList)
            await message.reply(file=discord.File("image/on9Water/" + image))
            
        if "垃圾殺菇咩" in message.content or "垃圾探女" in message.content  or "辣拉探女" in message.content: 
            emoji = get(self.bot.get_guild(652389840423354378).emojis, name="20201108100642")
            await message.reply(f"55ok {emoji}")
            
        if "сука" in message.content:
            await message.reply("блять")

        if "блять" in message.content:
            await message.reply("Пошёл нажуй даун ебаный ебал твою блять семью пидорасов СУКА БЛЯТЬ")

        if message.attachments and message.author == self.bot.get_user(400585510877396992) :
          emoji = get(self.bot.get_guild(652389840423354378).emojis, name="20201108100642")
          await message.reply(f"三井你有邊日唔係去玩同食好西 {emoji}")
          
def setup(bot):
    bot.add_cog(event(bot))