from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
from discord import File
import os
import traceback
import math

bot = commands.Bot(command_prefix='$')

class MatmaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def split(self, ctx, a:int, b:int):
        try:
            embed=discord.Embed(title="O to twoja liczba", description=(a//b), color=0xE657EE)
            return await ctx.send(embed=embed)
        except:
            e=discord.Embed(title="Liczba nie moze byc w ułamku dziesietnym", color=0xE657EE)
            await ctx.send(embed=e)

    @commands.command()
    async def multiply(self, ctx, a:int, b:int):
        try:
            embed=discord.Embed(title="O to twoja liczba", description=(a*b), color=0xE657EE)
            return await ctx.send(embed=embed)
        except:
            e=discord.Embed(title="Liczba nie moze byc w ułamku dziesietnym", color=0xE657EE)
            await ctx.send(embed=e)

    @commands.command()
    async def add(self, ctx, a:int, b:int):
        try:
            embed=discord.Embed(title="O to twoja liczba", description=(a+b), color=0xE657EE)
            return await ctx.send(embed=embed)
        except:
            e=discord.Embed(title="Liczba nie moze byc w ułamku dziesietnym", color=0xE657EE)
            await ctx.send(embed=e)
        

    @commands.command()
    async def remove(self, ctx, a:int, b:int):
        try:
            embed=discord.Embed(title="O to twoja liczba", description=(a-b), color=0xE657EE)
            return await ctx.send(embed=embed)
        except:
            e=discord.Embed(title="Liczba nie moze byc w ułamku dziesietnym", color=0xE657EE)
            await ctx.send(embed=e)
        

    @commands.command()
    async def pierwiastek(self, ctx, liczba:int=0):
        if liczba == 0:
            embed=discord.Embed(title="Nie podałeś liczby", color=0xE657EE)
            return await ctx.send(embed=embed)
        try:
            idk = math.sqrt(liczba)
            e=discord.Embed(title=f"Oto twoj pierwiastek ", color=0xE657EE)
            e.add_field(name="Pierwiastek:", value=(idk))
            await ctx.send(embed=e)
        except:
            await ctx.send(traceback.format_exc())
        
def setup(bot):
    bot.add_cog(MatmaCog(bot))
    print('Matma Gotowe')