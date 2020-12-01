import discord
from discord.ext import commands
import random
import array
import os
import os.path

bot = commands.Bot(command_prefix='!')
goldList = os.listdir("./image/goldImage")
sagumelist = os.listdir("./image/Sagume")
    
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(783286348144443404)
    await channel.send('少女讀取中...')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: 
        return

    with open('words/gumLee.txt', 'r' , encoding="utf-8")  as file:
        for line in file:
            if line.strip() in message.content:
                image = random.choice(goldlist)
                await message.channel.send("咁你有咩高見" )
                await message.channel.send(file=discord.File("image/goldImage" + image))
                return
    await bot.process_commands(message)

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
    await ctx.send('the bot is cool.')

@bot.command(name='殺菇')
async def mushroom(ctx ):
    await ctx.send('我要殺菇!')
    image = random.choice(sagumelist)
    await ctx.send(file=discord.File("image/Sagume/" + image))
    return





bot.run('')
