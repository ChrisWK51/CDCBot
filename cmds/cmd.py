import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import random
import json
import os
import os.path
from datetime import datetime as dt
from pytz import timezone as pt
from discord.utils import get
import urllib.request

with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)

sagumelist = os.listdir("./image/Sagume")
day = {
    "Mon": "星期一",
    "Tue": "星期二", 
    "Wed": "星期三", 
    "Thu": "星期四", 
    "Fri": "星期五",
    "Sat": "星期六",
    "Sun": "星期日",
}



class cmd(Cog_Extension):
    
    @commands.command(name='bot')
    async def _bot(self,ctx):
        
        image = random.choice(sagumelist)
        await ctx.reply('殺菇咩好耶 殺菇咩又中',file=discord.File("image/Sagume/" + image))

    @commands.command(name='殺菇')
    async def mushroom(self,ctx ):
        
        image = random.choice(sagumelist)
        await ctx.reply('我要殺菇!' , file=discord.File("image/Sagume/" + image))
    
    @commands.command()
    async def time(self,ctx):
        time = pt('HongKong').fromutc(dt.now())
        
        week = day[time.strftime('%a')]
        localTime = time.strftime(f'%Y年%m月%d日 {week} %X (GMT+8) ')
        await ctx.reply(f"月都依家既時間係 : {localTime}")

    @commands.command(name="0WaterTime")
    async def zerowatertime(self,ctx):
        pigWater = ""
        time = pt('Europe/London').fromutc(dt.now())
        week = day[time.strftime('%a')]
        localTime = time.strftime(f'%Y年%m月%d日 {week} %X (GMT) ')
        if (ctx.author == self.bot.get_user(174912315278229504)):
          ukHour = int(time.strftime('%H'))
          if ukHour >= 10  and ukHour <= 14 :
            pigWater = f"\n起身啦 鈴豬仲訓 {ctx.author.mention}"
          elif ukHour >= 0 and ukHour  <= 6:
            pigWater = f"\n鈴豬肯訓未 {ctx.author.mention}"
        await ctx.reply(f"鈴緒帝國依家既時間係 : {localTime + pigWater}")


    @commands.command(pass_context=True ,name="help")
    async def help(self,ctx):
        embed = discord.Embed(title=self.bot.user.name, description=f"{self.bot.description} \n 依家呢個殺菇bot有既command", color=0xC6CFD6)
        times = len(jdata["Command"])
        for i in range(times):
            embed.add_field(name="!" + jdata["Command"][i], value=jdata["Use"][i], inline=False)
        await ctx.reply(embed=embed)

    @commands.command()
    async def add(self , ctx , left : int, right : int):
        await ctx.reply(left + right)

    @commands.command()
    async def subtract(self , ctx , left : int, right : int):
        await ctx.reply(left - right)

    @commands.command()
    async def multiply(self , ctx , left : int, right : int):
        await ctx.reply(left * right)
    
    @commands.command()
    async def divide(self , ctx , left : int, right : int):
        if (left == 0 or right == 0):
            await ctx.reply("除唔到架 算把啦")
            return 
        await ctx.reply(left / right)
        
    @commands.command()
    async def modulus(self , ctx , left : int, right : int):
        if (left == 0 or right == 0):
            await ctx.reply("除唔到架 算把啦")
            return 
        await ctx.reply(left % right)

    @commands.command()
    async def roll(self , ctx, dice : str):
        rolls, limit = map(int, dice.split('d'))
        if rolls <= 0  or limit <= 0:
            await ctx.reply("出唔到架啦 算把啦")
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.reply(result)

    @commands.group(pass_context=True)
    async def cool(self , ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply('No, {0.subcommand_passed} is not cool'.format(ctx))

    @commands.command()
    async def info(self , ctx):
        embed = discord.Embed(title=self.bot.user.name, 
            description=f"{self.bot.description}\n\nMe: {self.bot.user.mention}" , color=0xC6CFD6 , 
        timestamp= dt.utcnow())

        createTime = pt('HongKong').fromutc(self.bot.user.created_at)
        createTime = createTime.strftime(f'%Y-%m-%d %X (GMT+8) ')
        currentTime = pt('HongKong').fromutc(dt.now())
        currentTime = currentTime.strftime(f'%Y-%m-%d %X (GMT+8) ')
        
        
        embed.set_author(name="KillMushroomBot Info", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Created at", value=f"{createTime}", inline=False)
        embed.add_field(name="KillMushroom.py timestamp", value=f"{currentTime}", inline=False)

        embed.add_field(name="Links", value=jdata["docInfo"], inline=False)
        embed.add_field(name="‎", value=jdata["botInvite"], inline=False)
        
        embed.add_field(name="Server Count", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Verison", value=jdata["Version"], inline=True)
        embed.add_field(name="Language", value="Python", inline=True)
        embed.set_footer(text=f"created by {self.bot.get_user(int(jdata['OwnerID']))}")
        await ctx.reply(embed=embed)

    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, input: str):
        if ctx.guild.me.guild_permissions.manage_messages:
            await ctx.message.delete()
        await ctx.send(input)
    
    @commands.command()
    async def luck(self, ctx):
        await ctx.reply(random.choice(jdata["luckList"]))

    @commands.command()
    async def clean(self , ctx, num ):
      if ctx.author.guild_permissions.administrator :
        #if num in "all":
        #    await ctx.channel.purge(limit=10000)
        #else:
        if ctx.guild.me.guild_permissions.manage_messages:
            num = int(num)
            await ctx.channel.purge(limit=num)
            await ctx.reply(f"殺菇咩幫你刪左 {num} 個messages.")
        else: 
            await ctx.reply("我冇特權 垃圾探女幫唔到你刪messages")
      else:
          await ctx.reply(jdata["LoadPermissionQuote"])

    @commands.command(name="三井")
    async def threeO(self,ctx):
      emoji = get(self.bot.get_guild(652389840423354378).emojis, name="20201108100642") 
      await ctx.send(f"{self.bot.get_user(400585510877396992).mention} 三井你有邊日唔係去玩 {emoji}")

    @commands.command(name="三井好西")
    async def three0(self,ctx):
      emoji = get(self.bot.get_guild(652389840423354378).emojis, name="20201108100642") 
      await ctx.send(f"{self.bot.get_user(400585510877396992).mention} 三井你有邊日唔係食好西 {emoji}")
    
    @commands.command(name="香港幾度")
    async def getTodayWeather(self,ctx):
      tempURL = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
      Result = urllib.request.urlopen(tempURL).read().decode()
      Result = json.loads(Result)
      temperature = Result["temperature"]["data"][1]["value"]
      ReturnString ="香港依家既温度係 "
      ReturnString += str(temperature) +"°" + Result["temperature"]["data"][1]["unit"] +"\n"
      if (temperature <= 15):
        ReturnString += f"香港仲未暖返啊 你就暖 {self.bot.get_user(174912315278229504).mention}"
      await ctx.reply(f"{ReturnString}")

def setup(bot):
    bot.add_cog(cmd(bot)) 
