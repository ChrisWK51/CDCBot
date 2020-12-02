import discord
from discord.ext import commands
import random
import array
import os
import os.path
from datetime import datetime as dt
import json

with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)

day = {
    "Mon": "星期一",
    "Tue": "星期二", 
    "Wed": "星期三", 
    "Thu": "星期四", 
    "Fri": "星期五",
    "Sat": "星期六",
    "Sun": "星期日",
}

bot = commands.Bot(command_prefix='!' , description="殺菇咩整出黎既殺菇咩bot \n 依家呢個殺菇bot有既command")
goldList = os.listdir("./image/goldImage")
sagumelist = os.listdir("./image/Sagume")
on9WaterList = os.listdir("./image/on9Water")

bot.remove_command('help')

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(int(jdata["Welcome_Channel"]))
    await channel.send('少女讀取中...')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: 
        return
    for i in jdata["goldenText"]:
        if i in message.content:
            image = random.choice(goldList)
            await message.channel.send("咁你有咩高見" , file=discord.File("image/goldImage/" + image))
            return
    for i in jdata["rubbishWater"]:
        msg = message.content.str.lower()
        if i in message.content:
            image = random.choice(on9WaterList)
            await message.channel.send(file=discord.File("image/on9Water/" + image))
            return

    if "垃圾殺菇咩" in message.content or "垃圾探女" in message.content:
        await message.channel.send(f"{message.author.mention} 55ok")
        return


    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=bot.user.name, description=bot.description, color=0xC6CFD6)
    times = len(jdata["Command"])
    for i in range(times):
        embed.add_field(name=jdata["Command"][i], value=jdata["Use"][i], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    await  ctx.send(bot.application_info())

@bot.command()
async def add(ctx , left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice : str):
    print('------')
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.group(pass_context=True)
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@bot.command(name='bot')
async def _bot(ctx):
    
    image = random.choice(sagumelist)
    await ctx.send('殺菇咩好耶 殺菇咩又中',file=discord.File("image/Sagume/" + image))
  

@bot.command(name='殺菇')
async def mushroom(ctx ):
    
    image = random.choice(sagumelist)
    await ctx.send('我要殺菇!' , file=discord.File("image/Sagume/" + image))
    
    return

@bot.command()
async def ping(ctx):
    await ctx.send(f"殺菇咩連地球既ping數係 : {round(bot.latency * 10)} ms")

@bot.command()
async def time(ctx):
    time = dt.now()
    
    week = day[time.strftime('%a')]
    localTime = time.strftime(f'%Y年%m月%d日 {week} %X (GMT+8) ')
    await ctx.send(f"月都依家既時間係 : {localTime}")

bot.run(jdata["TOKEN"])
