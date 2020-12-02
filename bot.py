import discord
from discord.ext import commands
import os
import os.path

import json
with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='!' , description="殺菇咩整出黎既殺菇咩bot \n 依家呢個殺菇bot有既command")

bot.remove_command('help')

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(int(jdata["Welcome_Channel"]))
    await channel.send('少女讀取中...')


@bot.command()
async def load(ctx , extension):
    if ctx.author.id == int(jdata["OwnerID"]) or ctx.author.guild_permissions.administrator:
        bot.load_extension(F'cmds.{extension}')
        await ctx.send(f"Loaded {extension} done")
    else:
        await ctx.send(jdata["LoadPermissionQuote"])
@bot.command()
async def unload(ctx , extension):
    if ctx.author.id == int(jdata["OwnerID"])  or ctx.author.guild_permissions.administrator:
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(f"Un - Loaded {extension} done")
    else:
        await ctx.send(jdata["LoadPermissionQuote"])
@bot.command()
async def reload(ctx , extension):
    if ctx.author.id == int(jdata["OwnerID"]) or ctx.author.guild_permissions.administrator:
        bot.reload_extension(F'cmds.{extension}')
        await ctx.send(f"Re - Loaded {extension} done")
    else:
        await ctx.send(jdata["LoadPermissionQuote"])

for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(jdata["TOKEN"])
