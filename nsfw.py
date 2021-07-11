from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
import json
from discord import File
import os

bot = commands.Bot(command_prefix='$')

class NsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lewdnekoooooo(self, ctx):    
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="O to twoje nagie nekośki zboczeńcu! HENTAI AND BAKA", color=0xE657EE) 
            embed.set_image(url=requests.get("https://nekos.life/api/v2/img/lewd").json()["url"])
            await ctx.send(embed=embed)
        if not ctx.channel.is_nsfw():
            embed = discord.Embed(title="Nie ma hentaiców bo zły kanał", color=0xE657EE)
            return await ctx.send(embed=embed)
            
    @commands.command()
    async def ahegoooooo(self, ctx):
        if ctx.channel.is_nsfw():
           embed=discord.Embed(title="O to twoje ahego zboczeńcu", color=0xE657EE)
           embed.set_image(url=requests.get("http://api.nekos.fun:8080/api/gasm").json()["image"])
           await ctx.send(embed=embed)
        if not ctx.channel.is_nsfw():
           embed = discord.Embed(title="Nie ma ahego bo zły kanał", color=0xE657EE)
           return await ctx.send(embed=embed)

    @commands.command()
    async def komendyNSFWooooo(self, ctx):
        embed = discord.Embed(title="KomendyNSFW", description="Lista komend NSFW:", color=0xE657EE)

        embed.add_field(name="$lewdneko", value="Wysyła nagie nekośki", inline=False)
        embed.add_field(name="$ahego", value="Wysyła obrazki ahego", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(NsfwCog(bot))
    print('NSFW Gotowe')