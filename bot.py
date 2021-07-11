import json
import requests
import cogs
import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import os
import jishaku

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"))

@bot.event
async def on_ready():
    print('Zalogowany jako')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game("$komendy"))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game("Bot włączony 24/7 lecz czasem zdarzają się problemy"))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game(f"Liczba serwerów: {len(bot.guilds)}"))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game("Mniam"))
    await asyncio.sleep(10)

@bot.command()
async def reload(ctx, arg):
    if ctx.author.id == 453950321790550016:
        try:
            bot.reload_extension(f"{arg}")
            await ctx.send(f"pomyslnie zrestartowano {arg}")
        except:
            embed=discord.Embed(title="Podales niewlasciwa nazwe cog'a\n{traceback.format_exc()}", color=0xE657EE)
            await ctx.send(embed=embed)
    if ctx.author.id == 327899255249436672:
        try:
            bot.reload_extension(f"{arg}")
            await ctx.send(f"pomyslnie zrestartowano {arg}")
        except:
            embed=discord.Embed(title=f"Podales niewlasciwa nazwe cog'a\n{traceback.format_exc()}", color=0xE657EE)
            await ctx.send(embed=embed)
    else:
        await ctx.send("nie masz dostepu")

@bot.command()
async def restart(ctx):
    try:
        if ctx.author.id == 453950321790550016:
            bot.reload_extension("fun")
            bot.reload_extension("lvls")
            bot.reload_extension("mod")
            bot.reload_extension("ddlc")
            bot.reload_extension("matma")
            bot.reload_extension("countryroulet")
            bot.reload_extension("todo")
            bot.reload_extension("info")
            bot.reload_extension("handler")
            bot.reload_extension("vip")
            bot.reload_extension("ping")
            bot.reload_extension("sex")
            bot.reload_extension("top")
            bot.reload_extension("eval")
            bot.reload_extension("Cos")
            bot.reload_extension("Pogoda")

            return await ctx.send("La restarione")

        if ctx.author.id == 327899255249436672:
            bot.reload_extension("fun")
            bot.reload_extension("lvls")
            bot.reload_extension("mod")
            bot.reload_extension("ddlc")
            bot.reload_extension("matma")
            bot.reload_extension("countryroulet")
            bot.reload_extension("todo")
            bot.reload_extension("handler")
            bot.reload_extension("info")
            bot.reload_extension("vip")
            bot.reload_extension("ping")
            bot.reload_extension("sex")
            bot.reload_extension("top")
            bot.reload_extension("eval")
            bot.reload_extension("Cos")
            bot.reload_extension("Pogoda")

            return await ctx.send("La restarione")

    except:
        embed=discord.Embed(title="chuj ci w dupe nie ma tak łatwo", color=0xE657EE)
        await ctx.send(embed=embed)

bot.remove_command('help')

bot.load_extension("fun")
bot.load_extension("lvls")
bot.load_extension("mod")
bot.load_extension("ddlc")
bot.load_extension("matma")
bot.load_extension("countryroulet")
bot.load_extension("handler")
bot.load_extension("info")
bot.load_extension("vip")
bot.load_extension("ping")
bot.load_extension("sex")
bot.load_extension("top")
bot.load_extension("eval")
bot.load_extension("komendy")

bot.run("")
