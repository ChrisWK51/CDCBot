import discord
from discord.ext import commands
import os
import os.path
import json
import keep_alive
with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!' , description="殺菇咩整出黎既殺菇咩bot" , intents=intents , case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(int(jdata["Welcome_Channel"]))


@bot.command()
async def load(ctx , extension):
    if ctx.author.id == int(jdata["OwnerID"]) or ctx.author.guild_permissions.administrator:
        bot.load_extension(F'cmds.{extension}')
        await ctx.reply(f"Loaded {extension} done")
    else:
        await ctx.reply(jdata["LoadPermissionQuote"])
@bot.command()
async def unload(ctx , extension):
    if ctx.author.id == int(jdata["OwnerID"])  or ctx.author.guild_permissions.administrator:
        bot.unload_extension(F'cmds.{extension}')
        await ctx.reply(f"Un - Loaded {extension} done")
    else:
        await ctx.reply(jdata["LoadPermissionQuote"])

@bot.command()
async def reload(ctx , extension):
    if ctx.author.id == int(jdata["OwnerID"]) or ctx.author.guild_permissions.administrator:
        bot.reload_extension(F'cmds.{extension}')
        await ctx.reply(f"Re - Loaded {extension} done")
    else:
        await ctx.reply(jdata["LoadPermissionQuote"])

for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.run(jdata["TOKEN"])
