import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import json,asyncio,datetime
from pytz import timezone as pt
import urllib.request
class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        ##self.counter = 0 
        #async def interval():
        #    await self.bot.wait_until_ready()
        #    self.channel = self.bot.get_channel(783286397632380928)
         #   while not self.bot.is_closed():
                #await self.channel.send("Hi I'm running!")
          #      await asyncio.sleep(5)

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(701294700094554262)
            while not self.bot.is_closed():
              now_time = pt('HongKong').fromutc(datetime.datetime.now()).strftime('%H%M')
              with open('setting.json','r' , encoding="utf-8") as jFile:
                  jdata = json.load(jFile)
              if now_time == jdata['time']  :          
                  await self.channel.send(getTodayWeather())
                  ##self.counter = 1
                  await asyncio.sleep(60)
              else:
                  await asyncio.sleep(1)
                  pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command(name="setchannel")
    async def set_channel(self, ctx , ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.reply(f"Set Channel: {self.channel.mention}")
    
    @commands.command()
    async def set_time(self, ctx, time):
        if int(time) > 2359 or int(time) < 0:
              await ctx.reply("用錯左啊 收皮啦")
              return 
        ##self.counter = 0 
        with open('setting.json','r' , encoding="utf-8") as jFile:
            jdata = json.load(jFile)
        jdata['time'] = time
        with open('setting.json','w' , encoding="utf-8") as jFile:
            json.dump(jdata,jFile,indent=4)
        await ctx.reply(f"Time successfully set")

def getTodayWeather():
    URL = 'http://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc'
    Result = urllib.request.urlopen(URL).read().decode()
    Result = json.loads(Result)
    ReturnString ="各位早晨  以下係殺菇咩帶俾你哋嘅天氣預報\n\n"
    for weather in Result:
        ReturnString += Result[weather] + "\n"
    return ReturnString

def setup(bot):
    bot.add_cog(Task(bot))