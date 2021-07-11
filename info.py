import discord
import cogs
import random
import asyncio
import requests
from discord import File
import os
import psutil
import humanize
import platform
import json
from discord.ext import commands, tasks
from itertools import cycle
import jishaku
import traceback
import time
import datetime
from gpiozero import CPUTemperature
import platform
import subprocess

bot = commands.Bot(command_prefix='$')

def uptime():
 
     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"
 
     total_seconds = float(contents[0])
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
     return string;
 

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botstats(self, ctx):
        cpu = CPUTemperature()
        d=int(psutil.virtual_memory().total)
        c=(d//1000//1000)
        ed=round(cpu.temperature, 1)
        e = discord.Embed(title="Statystyki bota:", description=f"Serwery: `{len(self.bot.guilds)}`\n\nKomendy: `{len(self.bot.commands)}`\n\nWersja Python: `{platform.python_version()}`\nWersja discord.py: `{discord.__version__}`\n\nWykorzystana pamięć RAM: `{humanize.naturalsize(psutil.Process().memory_full_info().rss)}/{c} MB`\nWłaściwości CPU: `{psutil.cpu_percent()}%`,`{ed}℃`, `{psutil.cpu_freq().current}Mhz`\nSystem: `{platform.uname().system}` `{platform.uname().node}`\n\nUptime:{uptime()}", color=0xE657EE)
        
        await ctx.send(embed=e)
    
    @commands.command()
    async def info(self, ctx):
        kucz= "```❤ Yes-Name ❤#6328```"
        vatheriner = "```Ge Fishe#5008```"
        embed = discord.Embed(title="Monika discord bot", description="Informacje", color=0xE657EE)
        embed.add_field(name="Autorzy", value=f"{kucz} {vatheriner}")
        embed.add_field(name="Kanał na Youtube Autora", value="https://www.youtube.com/channel/UCE-baC_N0skmfvn7a_3ZodA")
        embed.add_field(name="Liczba serwerów", value=f"{len(self.bot.guilds)}")
        embed.add_field(name="Invite", value="\[ [Zapros](https://discord.com/api/oauth2/authorize?client_id=707952241536925736&permissions=8&scope=bot) \]")
        embed.add_field(name="Vote", value="\[ [Za Voutuj](https://top.gg/bot/707952241536925736/vote) \]")
        embed.add_field(name="Donate", value="\[ [Donate](https://donatebot.io/checkout/790316194653536346?buyer=327899255249436672) \]")
        await ctx.send(embed=embed)

    @commands.command(aliases=['pong'])
    async def ping(self, ctx):
        embed=discord.Embed(title="🏓 Pong!", description=f"`{round(self.bot.latency * 1000)}` ms", color=0xE657EE)
        await ctx.send(embed=embed) 
    
    @commands.command()
    async def poll(self, ctx, *, arg):
        embed=discord.Embed(title=f"{arg}",color=0xE657EE)
        autor=ctx.author
        embed.set_footer(text=f"Ankieta wywołana przez {autor}")
        await ctx.message.delete()
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❎')
    
    @commands.command()
    async def ram(self, ctx):
        try:
            d=int(psutil.virtual_memory().total)
            c=(d//1000//1000)
            await ctx.send(f"{datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}\n{c}")
        except:
            await ctx.send(traceback.format_exc())

def setup(bot):
    bot.add_cog(InfoCog(bot))
    print('Info Gotowe')