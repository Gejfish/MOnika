from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
from discord import File
import os
from datetime import datetime
import traceback
import tabula
import json

bot = commands.Bot(command_prefix='$')

class VipCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chujwdupekuczkowiexe(self, ctx):
        try:           
            with open("planlekcji.json", "r") as f:
                pl = json.load(f)
            dzien = datetime.today().strftime('%A')

            if dzien == "Monday":
                embed=discord.Embed(title="plan lekcji Poniedzialek",description=str(pl["Monday"]), color=0xE657EE)
                embed.add_field(value=str(pl["Tuesday"]), name="Wtorek",inline=False)
                await ctx.send(embed=embed)

            if dzien == "Tuesday":
                embed=discord.Embed(title="Plan lekcji Wtorek", description=str(pl["Tuesday"]), color=0xE657EE)
                embed.add_field(value=str(pl["Wednesday"]), name="Sroda",inline=False)
                await ctx.send(embed=embed)

            if dzien == "Wednesday":
                embed=discord.Embed(title="Plan lekcji Sroda", description=str(pl["Wednesday"]), color=0xE657EE)
                embed.add_field(value=str(pl["Thursday"]), name="Czwartek",inline=False)
                await ctx.send(embed=embed)

            if dzien == "Thursday":
                embed=discord.Embed(title="Plan lekcji Czwartek", description=str(pl["Thursday"]), color=0xE657EE)
                embed.add_field(value=str(pl["Friday"]), name="Piatek",inline=False)
                await ctx.send(embed=embed)

            if dzien == "Friday":
                embed=discord.Embed(title="Plan lekcji Piatek", description=str(pl["Friday"]), color=0xE657EE)
                embed.add_field(value=str(pl["Monday"]), name="Poniedzialek",inline=False)
                await ctx.send(embed=embed)
        
        except:
                await ctx.send(traceback.format_exc())

    @commands.command()
    async def chujciwdupkekurwo(self, ctx, *, arg):
        try:
            await ctx.send(arg, tts=True)

        except:
            await ctx.send(f"```python\n{traceback.format_exc()}```")     

def setup(bot):
    bot.add_cog(VipCog(bot))
    print('Vip Gotowe')