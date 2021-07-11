from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
from discord import File
import os

bot = commands.Bot(command_prefix='$')

class RouletCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def countryroulet(self, ctx): 
        choices = ["Polska", "Francja", "Norwegia", "Szwecja", "Ukraina", "Egipt", "Finlandia", "Nepal", "Czechy", "Słowacja", "Wegry", "Holandia", "Austria", "Dania", "Peru", "Panama", "Kostaryka", "Argentyna", "Rosja", "USA", "Szwajcaria", "Litwa", "Irak", "Kazachstan", "Australia", "Kanada", "Meksyk", "Łotwa", "Estonia", "Hiszpania", "Wielka Brytania", "Białoruś", "Butan", "Chiny", "Niemcy", "Belgia", "Indie", "Rumunia", "Iran", "Brazylia"]
        kraj = random.choice(choices)
        embed=discord.Embed(title=(kraj), description=f"{ctx.author} Oto twój kraj", color=0xE657EE)
        if kraj == "Polska":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/0/06/Gjs.png/revision/latest/scale-to-width-down/220?cb=20180526052600&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Francja":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/b/bd/Franceballpeasant.png/revision/latest/scale-to-width-down/310?cb=20190928160725")
           return await ctx.send(embed=embed)
        if kraj == "Norwegia":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/d/db/Byz-R%C3%B8dt_Hvitt_og_Bl%C3%A5tt.png/revision/latest/scale-to-width-down/310?cb=20200830205259")
           await ctx.send(embed=embed)
        if kraj == "Szwecja":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/0/0f/Screen_Shot_2020-07-18_at_1.33.07_PM.png/revision/latest/scale-to-width-down/310?cb=20200718173409")
           return await ctx.send(embed=embed)
        if kraj == "Ukraina":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/5/5f/Ucraniaball_3.png/revision/latest?cb=20151228212112&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Egipt":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/a/a2/Egypt.jpg/revision/latest/scale-to-width-down/310?cb=20150327085553")
           return await ctx.send(embed=embed)
        if kraj == "Finlandia":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/3/3c/Suomi2.png/revision/latest/scale-to-width-down/310?cb=20170720163320")
           return await ctx.send(embed=embed)
        if kraj == "Nepal":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/e/ec/RAWRRAWRRAWR.png/revision/latest/scale-to-width-down/310?cb=20180924163340")
           return await ctx.send(embed=embed)
        if kraj == "Czechy":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/7/7a/Pivko_pivko_by_greencrossedball_dcs3l3z-fullview.jpg/revision/latest/scale-to-width-down/310?cb=20200520081420")
           return await ctx.send(embed=embed)
        if kraj == "Słowacja":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/8/88/SlovakiaHHH.jpeg/revision/latest/scale-to-width-down/310?cb=20180512182724")
           return await ctx.send(embed=embed)
        if kraj == "Węgry":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/d/d4/Magyar_stronk.png/revision/latest/scale-to-width-down/310?cb=20190201084328")
           return await ctx.send(embed=embed)
        if kraj == "Holoandia":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/e/e7/NDsDcbXs7F-8.png/revision/latest/scale-to-width-down/300?cb=20180531132433")
           return await ctx.send(embed=embed)
        if kraj == "Austria":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/6/61/OsterreicheditKG.png/revision/latest/scale-to-width-down/228?cb=20201006055220")
           return await ctx.send(embed=embed)
        if kraj == "Dania":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/1/1c/Dinamarcaball_1.png/revision/latest/scale-to-width-down/200?cb=20160228113117&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Peru":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/4/4f/19437344_723689921136132_8292754126687580144_n.png/revision/latest/scale-to-width-down/310?cb=20200921172730")
           return await ctx.send(embed=embed)
        if kraj == "Panama":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/0/00/Panamaball.png/revision/latest/scale-to-width-down/400?cb=20170109142455")
           return await ctx.send(embed=embed)    
        if kraj == "Kostaryka":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/f/ff/Costa_Ricaball_%28FB%29.png/revision/latest?cb=20190420201223")
           return await ctx.send(embed=embed)
        if kraj == "Argentyna":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/1/11/LosArgentinosSonSuperiores.png/revision/latest?cb=20181101041549")
           return await ctx.send(embed=embed)
        if kraj == "Rosja":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/6/60/RU.png/revision/latest/scale-to-width-down/218?cb=20190903165752")
           return await ctx.send(embed=embed)
        if kraj == "USA":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/e/e8/USAball.png/revision/latest/scale-to-width-down/239?cb=20191206215024")
           return await ctx.send(embed=embed)
        if kraj == "Szwajcaria":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/e/e3/Switzerland-neutral-look.png/revision/latest/scale-to-width-down/310?cb=20181022011240")
           return await ctx.send(embed=embed)
        if kraj == "Litwa":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/4/43/Lituaniaball.png/revision/latest?cb=20151228191013&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Kazachstan":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/1/15/Kazakh.png/revision/latest/scale-to-width-down/300?cb=20160228144944&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Irak":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/3/35/Iraqball_-_Polandball_Cup.png/revision/latest/scale-to-width-down/310?cb=20170312124625")
           return await ctx.send(embed=embed)
        if kraj == "Australia":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/4/48/Australianball.jpg/revision/latest/scale-to-width-down/310?cb=20170125190116")
           return await ctx.send(embed=embed)
        if kraj == "Kanada":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/9/90/Kanada.png/revision/latest/scale-to-width-down/310?cb=20160227183853&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Meksyk":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/9/9f/Meksyk.png/revision/latest?cb=20160730113120&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Łotwa":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/5/58/10013407_225633494292302_2129667750_o.png/revision/latest/scale-to-width-down/310?cb=20151228185348&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Estonia":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/0/08/Th-9-.jpg/revision/latest?cb=20181014205909&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Hiszpania":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/5/58/Spain.png/revision/latest/scale-to-width-down/300?cb=20160408172148&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Wielka Brytania":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/d/d5/RUballe.png/revision/latest/scale-to-width-down/310?cb=20151228214535&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Białoruś":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/8/81/Byz-White_Ruthenia.png/revision/latest/scale-to-width-down/310?cb=20200819183810")
           return await ctx.send(embed=embed)
        if kraj == "Butan":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/3/3a/Byz-Crazy_Monk.png/revision/latest/scale-to-width-down/310?cb=20200105232241")
           return await ctx.send(embed=embed)
        if kraj == "Chiny":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/9/9c/DynastyChinaball.jpg/revision/latest/scale-to-width-down/120?cb=20170117144500")
           return await ctx.send(embed=embed)
        if kraj == "Niemcy":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/f/fe/Germanyball_%289%29.png/revision/latest/scale-to-width-down/310?cb=20160226203616&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Belgia":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/8/8d/Belgium_ball.png/revision/latest/scale-to-width-down/300?cb=20190310172854&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Indie":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/7/76/11010619_979614238717838_5592672150556764188_n.jpg/revision/latest/scale-to-width-down/310?cb=20160819172748")
           return await ctx.send(embed=embed)
        if kraj == "Rumunia":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/5/55/Gibgib.png/revision/latest/scale-to-width-down/300?cb=20160420112843&path-prefix=pl")
           return await ctx.send(embed=embed)
        if kraj == "Iran":
           embed.set_image(url="https://static.wikia.nocookie.net/polandball/images/1/1f/Iranball_%281%29.png/revision/latest/scale-to-width-down/310?cb=20170224113720")
           return await ctx.send(embed=embed)
        if kraj == "Brazylia":
           embed.set_image(url="https://vignette.wikia.nocookie.net/polandball/images/e/e2/Sketch-1460212721846.png/revision/latest/zoom-crop/width/240/height/240?cb=20160409144114&path-prefix=pl")
           return await ctx.send(embed=embed)
         
def setup(bot):
    bot.add_cog(RouletCog(bot))
    print('Ruletka Gotowe')