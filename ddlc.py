from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
from discord import File
import os

bot = commands.Bot(command_prefix='$')

class DdlcCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def infomonika(self, ctx):
        embed = discord.Embed(title="Informacje o Monice", color=0xE657EE)

        embed.add_field(name="Imię", value="Monika", inline=False)
        embed.add_field(name="Wiek", value="18 (urodziny 22 września)", inline=False)
        embed.add_field(name="Lubi", value="Gracza, Klub Literacki, wiersze, grę na pianinie", inline=False)
        embed.add_field(name="Nie lubi", value="Doki Doki Literature Club! (gry)", inline=False)
        embed.add_field(name="Wzrost", value="160cm", inline=False)
        embed.add_field(name="Płeć", value="Kobieta", inline=False)
        embed.add_field(name="Kolor włosów", value="Koralowy brąz", inline=False)
        embed.add_field(name="Kolor oczu", value="Szmaragdowa zieleń", inline=False)
        embed.add_field(name="Klub", value="Klub Literacki (przewodnicząca)", inline=False)
        embed.set_image(url=("https://cdn.discordapp.com/attachments/601341984803651608/840667166914379836/artworks-000254624831-37rr44-t500x500.png"))

        await ctx.send(embed=embed)

    @commands.command()
    async def infoyuri(self, ctx):
        embed = discord.Embed(title="Informacje o Monice", color=0xE657EE)

        embed.add_field(name="Imię", value="Yuri", inline=False)
        embed.add_field(name="Wiek", value="18", inline=False)
        embed.add_field(name="Lubi", value="Książki, książki psychologiczne, horrory, noże, herbatę", inline=False)
        embed.add_field(name="Nie lubi", value="przeszkadzać innym, bólów kręgosłupa, zwracać na siebie uwagę", inline=False)
        embed.add_field(name="Wzrost", value="165cm", inline=False)
        embed.add_field(name="Płeć", value="Kobieta", inline=False)
        embed.add_field(name="Kolor włosów", value="Ciemny fiolet", inline=False)
        embed.add_field(name="Kolor oczu", value="Jasny fiolet", inline=False)
        embed.add_field(name="Klub", value="Klub Literacki (członek), (wiceprzewodnicząca w Akcie 2 i 4)", inline=False)
        embed.set_image(url=("https://vignette.wikia.nocookie.net/doki-doki-literature-club/images/7/72/Yuri_school_1.png/revision/latest?cb=20171112095243"))

        await ctx.send(embed=embed)

    @commands.command()
    async def infosayori(self, ctx):
        embed = discord.Embed(title="Informacje o Sayori", color=0xE657EE)

        embed.add_field(name="Imię", value="Sayori", inline=False)
        embed.add_field(name="Wiek", value="18", inline=False)
        embed.add_field(name="Lubi", value="Ciastka, przeszkadzać innym, zwracać na siebie uwagę", inline=False)
        embed.add_field(name="Nie lubi", value="Samotności", inline=False)
        embed.add_field(name="Wzrost", value="157cm", inline=False)
        embed.add_field(name="Płeć", value="Kobieta", inline=False)
        embed.add_field(name="Kolor włosów", value="Koralowy róż", inline=False)
        embed.add_field(name="Kolor oczu", value="Błękit", inline=False)
        embed.add_field(name="Klub", value="Klub Literacki (członek), (wiceprzewodniczącą (w akcie 1) lub przewodniczącą (w akcie 4) )", inline=False)
        embed.set_image(url=("https://vignette.wikia.nocookie.net/doki-doki-literature-club-pl/images/a/a6/Sayori.png/revision/latest?cb=20180411162813&path-prefix=pl"))

        await ctx.send(embed=embed)

    @commands.command()
    async def infonatsuki(self, ctx):
        embed = discord.Embed(title="Informacje o Monice", color=0xE657EE)

        embed.add_field(name="Imię", value="Natsuki", inline=False)
        embed.add_field(name="Wiek", value="18 ", inline=False)
        embed.add_field(name="Lubi", value="Piec ciastka", inline=False)
        embed.add_field(name="Nie lubi", value="Zwracać na siebie uwagi", inline=False)
        embed.add_field(name="Wzrost", value="149cm", inline=False)
        embed.add_field(name="Płeć", value="Kobieta", inline=False)
        embed.add_field(name="Kolor włosów", value="Pastelowy róż", inline=False)
        embed.add_field(name="Kolor oczu", value="Róż", inline=False)
        embed.add_field(name="Klub", value="Klub Literacki (członek)", inline=False)
        embed.set_image(url=("https://vignette.wikia.nocookie.net/doki-doki-literature-club-pl/images/b/bd/Natsuki.png/revision/latest?cb=20180411161828&path-prefix=pl"))

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(DdlcCog(bot))
    print('DDLC Gotowe')