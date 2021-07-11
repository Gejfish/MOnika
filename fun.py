from asyncio.tasks import wait
from discord import integrations
from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
import json
from datetime import datetime
import urllib.parse
from discord import File
import aiohttp
import os
from PIL import Image
import traceback
import time
from discord.ext import tasks, commands  
import calendar
import threading
from multiprocessing.pool import ThreadPool

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def howhomo(self, ctx, member: discord.User=None):  
        member = member or ctx.author
        if not member:
            embed=discord.Embed(title="Nie podano użytkownika", color=0xE657EE)
            await ctx.send(embed=embed)
        if member:
           sex = requests.get(f"https://some-random-api.ml/canvas/gay?avatar=https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png").content
           open("sex.png", "wb").write(sex)
           file = discord.File("sex.png") 
           embed=discord.Embed(title=f"{member.name} jest homo w {random.randint(0, 100)}%!", file=File("sex.png"), color=0xE657EE)
           embed.set_image(url="attachment://sex.png")
           await ctx.send(embed=embed, file=file)
        
    @commands.command(aliases=["mc"])
    async def achievement(self, ctx, *, arg):            
        arg = arg.replace(" ", "+").replace("ś", "s").replace("ę", "e").replace("ż", "z").replace("ź", "z").replace("ł", "l").replace("ó", "o").replace("ą", "a").replace("ć", "c").replace("Ś", "S").replace("Ę", "E").replace("Ż", "Z").replace("Ź", "Z").replace("Ł", "L").replace("Ó", "O").replace("Ą", "A").replace("Ć", "C")
        img = requests.get(f"https://minecraftskinstealer.com/achievement/{random.randint(1, 40)}/Achievement+Get%21/{arg}").content
        open("achievement.png", "wb").write(img)
        await ctx.send(file=File("achievement.png"))
        os.remove("achievement.png")

    @commands.command(aliases=["bz"])
    async def binaryzamiana(self, ctx, *, arg):
        arg = arg.replace(" ", "+").replace("ś", "s").replace("ę", "e").replace("ż", "z").replace("ź", "z").replace("ł", "l").replace("ó", "o").replace("ą", "a").replace("ć", "c").replace("Ś", "S").replace("Ę", "E").replace("Ż", "Z").replace("Ź", "Z").replace("Ł", "L").replace("Ó", "O").replace("Ą", "A").replace("Ć", "C")
        Tekst=requests.get(f"https://some-random-api.ml/binary?text={arg}").json()
        e=discord.Embed(title="Oto Twoj tekst w kodzie binarnym", description=str(Tekst["binary"]),color=0xE657EE)
        await ctx.send(embed=e)

    @commands.command(aliases=["bd"])
    async def binarydecode(self, ctx, *, arg):
        try:
            if arg == complex:
                print("rozjebane")
            if not arg == complex:
                Tekst=requests.get(f"https://some-random-api.ml/binary?decode={arg}").json()
                e=discord.Embed(title="Oto Twoj tekst z kodu binarnego", description=str(Tekst["text"]),color=0xE657EE)
                await ctx.send(embed=e)
        except:
            await ctx.send(traceback.format_exc())

    @commands.command()
    async def worsethan(self, ctx,  me: discord.User=None):

        me = me or ctx.author

        open("member41.png", "wb").write(requests.get(me.avatar_url).content)
            
        para = Image.open("xxlb4l9bfgi31.png")
        member1 = Image.open("member41.png")
            
        new_image = member1.resize((200, 230))
        
        para.paste(new_image, (54, 40))

        para.save("erika.png")
            
        await ctx.send(file=discord.File("erika.png"))

    @commands.command()
    async def randomn(self, ctx, od: int, do: int):
        embed=discord.Embed(title=f"Losowa liczba: {random.randint(od, do)}", color=0xE657EE)
        await ctx.send(embed=embed)

    @commands.command()
    async def feed(self, ctx, member: discord.User=None):
        if not member:
            embed=discord.Embed(title="Nie możesz nakarmić ducha", color=0xff3399)
            sex = "https://images-ext-2.discordapp.net/external/cvzmgzntjU0BeMHEfEx71DO4OSgpSjK7my80EF7qDnc/https/cdn.zerotwo.dev/SAD/edc5f5a4-cb77-47cd-b22a-faea0cad0b65.gif"
            embed.set_image(url=(sex))
            await ctx.send(embed=embed)
        if member:
           embed=discord.Embed(title=f"**{ctx.author.name}** nakarmił/a **{member.name}**!", color=0xE657EE)
           embed.set_image(url=requests.get("http://api.nekos.fun:8080/api/feed").json()["image"])
           await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.User=None):    
        if not member:
            embed=discord.Embed(title="Nie możesz pocałować ducha", color=0xff3399)
            sex = "https://images-ext-2.discordapp.net/external/cvzmgzntjU0BeMHEfEx71DO4OSgpSjK7my80EF7qDnc/https/cdn.zerotwo.dev/SAD/edc5f5a4-cb77-47cd-b22a-faea0cad0b65.gif"
            embed.set_image(url=(sex))
            await ctx.send(embed=embed)
        if member:
           embed = discord.Embed(title=f"**{ctx.author.name}** pocałował/a **{member.name}**!", color=0xE657EE) 
           embed.set_image(url=requests.get("https://nekos.life/api/kiss").json()["url"])
           return await ctx.send(embed=embed)

    @commands.command()
    async def beautiful(self, ctx,  me: discord.User=None):

        me = me or ctx.author

        open("member1.png", "wb").write(requests.get(me.avatar_url).content)
            
        para = Image.open("memeb.png")
        member1 = Image.open("member1.png")
        member2 = Image.open("member1.png")
            
        member1.thumbnail((90, 90))
        member2.thumbnail((87, 87))
        
        para.paste(member1, (203, 15))
        para.paste(member2, (212, 183))

        para.save("erika.png")
            
        await ctx.send(file=discord.File("erika.png"))

    @commands.command()
    async def dog(self, ctx):
        embed=discord.Embed(title="Pieseł :dog:!", color=0xE657EE)
        embed.set_image(url=requests.get("https://dog.ceo/api/breeds/image/random").json()["message"])
        await ctx.send(embed=embed)

    @commands.command()
    async def neko(self, ctx):    
        embed = discord.Embed(title="O to twoje nekośki UwU", color=0xE657EE) 
        embed.set_image(url=requests.get("https://nekos.life/api/neko").json()["neko"])
        return await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member: discord.User=None):    
        if not member:
            embed=discord.Embed(title="Nie możesz pogłaskać ducha", color=0xff3399)
            sex = "https://images-ext-2.discordapp.net/external/cvzmgzntjU0BeMHEfEx71DO4OSgpSjK7my80EF7qDnc/https/cdn.zerotwo.dev/SAD/edc5f5a4-cb77-47cd-b22a-faea0cad0b65.gif"
            embed.set_image(url=(sex))
            await ctx.send(embed=embed)
        if member:
           embed = discord.Embed(title=f"**{ctx.author.name}** pogłaskał/a **{member.name}**!", color=0xE657EE)
           embed.set_image(url=requests.get("https://nekos.life/api/pat").json()["url"])
           return await ctx.send(embed=embed)
        
    @commands.command()
    async def legia(self, ctx):
        embed=discord.Embed(title="", description="Legia to chuje, a Lech mistrz Polski Nasza duma Wielkopolski Oko za oko, mistrzostwo za ząb Kolejorz mistrzem jest co rok Legia to chuje, a Lech mistrz Polski Nasza duma Wielkopolski Oko za oko, mistrzostwo za ząb Kolejorz mistrzem jest co rok", color=0xE657EE)
        legia = "https://i.pinimg.com/236x/65/ba/55/65ba550a8ac5c5671262fa11bc20a6c5--emblem-logo-sports-logos.jpg"
        embed.set_image(url=(legia))
        return await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        embed=discord.Embed(title="Koteł :cat:!", color=0xE657EE)
        embed.set_image(url=requests.get("https://some-random-api.ml/img/cat").json()["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
        embed=discord.Embed(title="Panda OwO", color=0xE657EE)
        embed.set_image(url=requests.get("https://some-random-api.ml/img/panda").json()["link"])
        await ctx.send(embed=embed)    

    @commands.command()
    async def redpanda(self, ctx):
       embed=discord.Embed(title="Czerwona panda!", color=0xE657EE)
       embed.set_image(url=requests.get("https://some-random-api.ml/img/red_panda").json()["link"])
       await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
        icon = (ctx.author.guild.icon_url)
        embed=discord.Embed(title='Oto twoja ikona servera', color=0xE657EE)
        embed.set_image(url=(icon))
        await ctx.send(embed=embed)

    @commands.command(aliases=["8ball", "8bal"])
    async def _8ball(self, ctx):
        choices = ["A jeszcze jak", "Nie wiem", "Nie", "Tak", "Może", "Na pewno tak", "Na pewno nie"]
        ball = random.choice(choices)
        embed=discord.Embed(title=":8ball: Hmmm", description=str(ball), color=0xE657EE)
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, m: discord.Member=None):
        if not m:
            m = ctx.author
        e = discord.Embed(description=f"Prosze UwU:\n{m}", color=0xE657EE)
        e.set_thumbnail(url=m.avatar_url)
        await ctx.send(embed=e)

    @commands.command()
    async def coinflip(self, ctx):
        choices = ["Orzeł", "Reszka"]
        rancoin = random.choice(choices)
        embed=discord.Embed(title=(rancoin), description=f"{ctx.author} Brawo!", color=0xE657EE)
        return await ctx.send(embed=embed)    

    @commands.command()
    async def religia(self, ctx):
        choices = ["Rzymsko-Katolizm", "Prawosławie", "Protestantyzm", "Ateista", "Hinduizm", "Islam", "Judaizm", "Buddyzm", "Fetyszyzm" ]
        religion = random.choice(choices)
        embed=discord.Embed(title=(religion), description=f"{ctx.author} Oto twoja religia", color=0xE657EE)
        return await ctx.send(embed=embed)

    @commands.command()
    async def ideologia(self, ctx):
        choices = ["Faszyzm", "Komunizm", "Nazizm", "Liberalizm", "Demokracja", "Monarchia", "Anarchizm", "Kapitalizm", "Socjalizm", "Nacjonalizm"]
        ideology = random.choice(choices)
        embed=discord.Embed(title=(ideology), description=f"{ctx.author} Oto twoja ideologia", color=0xE657EE)
        return await ctx.send(embed=embed)    
    
    @commands.command()
    async def chucknorris(self, ctx):
        choices = ["Das Loch in der Ozonschicht entwickelte sich nur, weil Chuck Norris entschied, dass eine dunklere Bräune gut an ihm aussehen würde.", "Als Chuck Norris ein Teenager war, benutzten seine Eltern einen Presslufthammer, um seine Pickel zu entfernen.", "Cuando Chuck Norris era un adolescente, sus padres usaron un martillo neumático para extirpar sus granos.", "Chuck Norris ergenlik çağındayken, ebeveynleri sivilcelerini tüketmek için bir çekiç kullanıyordu.", "Everybody thinks the Galaxy Note 7 is explosive. In fact it is only Chuck Norris who tries to send a WhatsApp message with a selfie to his fans", "Все думают, что Galaxy Note 7 взрывоопасен. На самом деле, только Чак Норрис пытается отправить сообщение фанатам WhatsApp с селфи", ]
        chucknorris = random.choice(choices)
        embed=discord.Embed(title= "Oto twoje żarty o chacku norrisie w rożnych jezykach ", description =(chucknorris), color=0xE657EE)
        return await ctx.send(embed=embed)

    @commands.command()
    async def anime(self, ctx):
        papuga = requests.get("http://127.0.0.1:5000/anime-char").json()
        embed=discord.Embed(title=(papuga["name"]), color=0xE657EE)
        embed.set_image(url=papuga["image"])
        await ctx.send(embed=embed)    

    @commands.command()
    async def slap(self, ctx, *, member: discord.User=None):
        if not member:
            embed=discord.Embed(title="Nie możesz uderzyć ducha", color=0xff3399)
            sex = "https://images-ext-2.discordapp.net/external/cvzmgzntjU0BeMHEfEx71DO4OSgpSjK7my80EF7qDnc/https/cdn.zerotwo.dev/SAD/edc5f5a4-cb77-47cd-b22a-faea0cad0b65.gif"
            embed.set_image(url=(sex))
            await ctx.send(embed=embed)
        if member:
            embed=discord.Embed(title=f"**{ctx.author.name}** uderzył/a **{member.name}**!", color=0xE657EE)
            embed.set_image(url=requests.get("http://api.nekos.fun:8080/api/slap").json()["image"])
            await ctx.send(embed=embed)    

    @commands.command()
    async def hug(self, ctx, member: discord.User=None):
        if not member:
            embed=discord.Embed(title="Nie możesz przytulić ducha", color=0xff3399)
            sex = "https://images-ext-2.discordapp.net/external/cvzmgzntjU0BeMHEfEx71DO4OSgpSjK7my80EF7qDnc/https/cdn.zerotwo.dev/SAD/edc5f5a4-cb77-47cd-b22a-faea0cad0b65.gif"
            embed.set_image(url=(sex))
            await ctx.send(embed=embed)
        if member:
            embed=discord.Embed(title=f"**{ctx.author.name}** przytulił/a **{member.name}**!", color=0xE657EE)
            embed.set_image(url=requests.get("https://some-random-api.ml/animu/hug").json()["link"])
            await ctx.send(embed=embed)

    @commands.command()
    async def memy(self, ctx):
        try:
            if not ctx.channel.is_nsfw():
                embed=discord.Embed(title="Nie mozesz tutaj tego wysłać ponieważ kanał nie jest nsfw", color=0xE657EE)
                return await ctx.send(embed=embed)
            d = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            e=discord.Embed(title="Oto twoj mem", color=0xE657EE)
            e.set_image(url=requests.get("https://cenzurabot.pl/api/memes/jbzd").json()["meme"])
            e.set_footer(text=f"URL do api https://cenzurabot.pl/api/memes/jbzd.")
            await ctx.send(embed=e)
        except:
            await ctx.send(traceback.format_exc())

    @commands.command(aliases=["g"])
    async def google(self, ctx, *, search=None):
        if not search:
            embed=discord.Embed(title="Nie podałeś niczego do wyszukania", color=0xE657EE)
            await ctx.send(embed=embed)
        if search:
            embed=discord.Embed(title="Wynik", color=0xE657EE)
            embed.add_field(name='Twój wynik wyszukiwania:', value=f'https://google.com/search?q={urllib.parse.quote_plus(search)}', inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def twitch(self, ctx, *, arg=None):
        try:
            if not arg:
                embed=discord.Embed(title="Nie podałeś niczego do wyszukania", color=0xE657EE)
                await ctx.send(embed=embed)
            if arg:
                arg = arg.replace(" ", "%20").replace("ś", "s").replace("ę", "e").replace("ż", "z").replace("ź", "z").replace("ł", "l").replace("ó", "o").replace("ą", "a").replace("ć", "c").replace("Ś", "S").replace("Ę", "E").replace("Ż", "Z").replace("Ź", "Z").replace("Ł", "L").replace("Ó", "O").replace("Ą", "A").replace("Ć", "C")
                e=discord.Embed(title="Wynik",description=f"https://www.twitch.tv/search?term={arg}", color=0xE657EE)
                await ctx.send(embed=e)
        except:
            await ctx.send(traceback.format_exc())

    @commands.command()
    async def kalendarz(self, ctx):
        try:
            rok = time.strftime("%Y", time.localtime())
            mies = time.strftime("%m", time.localtime())
            dzien = time.strftime("%d", time.localtime())
            ro1= int(rok)
            m1=int(mies)
            dzi = int(dzien)
            cal = calendar.month(ro1, m1)
            d=cal.replace("Mo","Pn").replace("Tu","Wt").replace("We","Sr").replace("Th","Cz").replace("Fr","Pi").replace("Sa","Sb").replace("Su","Nd").replace("January ","Styczeń").replace("February","Luty").replace("March","Marzec").replace("April","Kwiecień").replace("May","Maj").replace("June","Czerwiec").replace("July","Lipiec").replace("August","Sierpień").replace("September","Wrzesień").replace("October","Październik").replace("November","Listopad").replace("December","Grudzień").replace(f" {dzi} ",f"[{dzi}]")
            await ctx.send(f"```css\n{d}```")
        except:
            await ctx.send(traceback.format_exc())

    @commands.command(aliases=["yt"])
    async def youtube(self, ctx, *, arg=None):
        if not arg:
            embed=discord.Embed(title="Nie podałes niczego do wyszukania", color=0xE657EE)
            await ctx.send(embed=embed)
        if arg:
            arg = arg.replace(" ", "+").replace("ś", "s").replace("ę", "e").replace("ż", "z").replace("ź", "z").replace("ł", "l").replace("ó", "o").replace("ą", "a").replace("ć", "c").replace("Ś", "S").replace("Ę", "E").replace("Ż", "Z").replace("Ź", "Z").replace("Ł", "L").replace("Ó", "O").replace("Ą", "A").replace("Ć", "C")
            embed=discord.Embed(title="Wynik", color=0xE657EE)
            embed.add_field(name='Twój wynik wyszukiwania:', value=f'https://www.youtube.com/results?search_query={arg}', inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def ytcomment(self, ctx, *, text=None):
        try:
            member=ctx.author
            img=requests.get(f"https://some-random-api.ml/canvas/youtube-comment?comment={text}&username={ctx.message.author.name}&avatar={member.avatar_url_as(format='png')}").content
            em=discord.Embed(title="Oto twój komentarz", color=0xE657EE)
            em.set_image(url=img)
            await ctx.send(embed=em)
        except:
            await ctx.send(traceback.format_exc())

    @commands.command()
    async def say(self, ctx, *, arg=None):
        if not arg:
            embed=discord.Embed(title="Nie podałeś tekstu", color=0xE657EE)
            return await ctx.send(embed=embed)
        if arg:
            arg = arg.replace("@", "@\u200b")
            await ctx.message.delete()
            await ctx.send(arg)
           
    @commands.command(pass_context = True)
    async def esay(self, ctx, *args, amount=0):
        if not args:
            embed=discord.Embed(title="Nie podałeś żadnego tekstu", color=0xE657EE)
            return await ctx.send(embed=embed)
        if args:
           await ctx.channel.purge(limit=amount + 1)
           mesg = ' '.join(args)
           embed=discord.Embed(title=(mesg), color=0xE657EE)
           embed.set_footer(text=f"{ctx.author}")
           await ctx.send(embed=embed)
           
    @commands.command()
    async def trigger(self, ctx, member: discord.User=None):
        member = member or ctx.author
        sex = requests.get(f"https://some-random-api.ml/canvas/triggered?avatar=https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png").content
        open("cos.gif", "wb").write(sex)
        file = discord.File("cos.gif") 
        embed = discord.Embed(title="Triggered wrrr", file=File("cos.gif"), color=0xff3399) 
        embed.set_image(url="attachment://cos.gif")
        return await ctx.send(embed=embed, file=file)
        os.remove("cos.gif")

    @commands.command() # adding a aliase to the command so we can use !lyrc or !lyrics
    async def lyrics(self, ctx, *, search=None):
        """A command to find lyrics easily!"""
    
        if not search: # if user hasnt typed anything, throw a error
            embed = discord.Embed(title="Nie podales nazwy!", color=0xE657EE)
            await ctx.reply(embed=embed)
            
            # ctx.reply is available only on discord.py 1.6.0!
            
        song = search.replace(' ', '%20') # replace spaces with "%20"
        
        async with aiohttp.ClientSession() as lyricsSession: # define session
            async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: # define json data
                if not (300 > jsondata.status >= 200):
                    await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
                else:
                    lyricsData = await jsondata.json() # load json data
            songLyrics = lyricsData['lyrics'] # the lyrics
            songArtist = lyricsData['author'] # the authors name
            songTitle = lyricsData['title'] # the songs title
            
            try:
                for chunk in [songLyrics[i:i+2000] for i in range(0, len(songLyrics), 2000)]: # if the lyrics extend the discord character limit (2000): split the embed
                    embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=0xE657EE)
                    embed.timestamp = datetime.utcnow()
                    
                    await lyricsSession.close() # closing the session
                    
                    await ctx.send(embed=embed)
                    
            except discord.HTTPException:
                embed = discord.Embed(title=f'{songTitle} przez {songArtist}', description=chunk, color=0xE657EE)
                embed.timestamp = datetime.utcnow()
                
                await lyricsSession.close() # closing the session
                
                await ctx.send(embed=embed)
                
    @commands.command()
    async def losowanie(self, ctx, *, arg=None):
        if not arg:
            e=discord.Embed(title="Nie podales slow", color=0xE657EE)
            await ctx.send(embed=e)
        if arg:
            chuj = arg.split()
            los = random.choice(chuj)
            e=discord.Embed(title="O to twoje losowanie", description=f"{los}", color=0xE657EE)
            await ctx.send(embed=e)
            
    @commands.command()
    async def kuczeg(self, message):
        args = message.content.split(" ")[1:]
        await self.delete_message(message)
        await self.send_message(message.channel, " ".join(args))

    @commands.command()
    async def pogoda(self, ctx, *, arg=None):
        if arg == None:
            embed=discord.Embed(title='Nie podales miasta', color=0xE657EE)
            return await ctx.send(embed=embed)

        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={arg}&lang=pl&appid=5e3b4b16fee3823d2b049bc107fc257a&units=metric'
            chuj = requests.get(url).json()
            embed=discord.Embed(title=str(chuj["name"]), color=0xE657EE)
            embed.set_thumbnail(url="https://ssl.gstatic.com/onebox/weather/64/partly_cloudy.png")
            embed.add_field(value=chuj['weather'][0]['description'], name='Pogoda', inline=False)
            embed.add_field(value=str(chuj['main']['temp'])+"℃", name='Temperatura', inline=False)
            embed.add_field(value=str(chuj['main']['feels_like'])+'℃', name='Odczuwana temperatura', inline=False)
            embed.add_field(value=str(chuj['main']['temp_min'])+'℃', name='Temperatura minimalna', inline=False)
            embed.add_field(value=str(chuj['main']['pressure'])+'hPa', name='Cisnienie', inline=False)
            embed.add_field(value=str(chuj['main']['humidity'])+'%', name='Wilgotnosc', inline=False)
            embed.add_field(value=str(chuj['wind']['speed'])+'km/h', name='Prędkość wiatru', inline=False)
            embed.add_field(value=str(chuj['clouds']['all'])+'%', name='Zachmurzenie', inline=False)
            embed.add_field(value=str(chuj['sys']['country']), name='Kraj', inline=False)
            await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="Error", description=f"problem z zwróceniem pogody z {arg}", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def coronovirus(self, ctx, member: discord.User=None):
        try:
            member = member or ctx.author
            opcje=["Ma coronovirusa","Nie ma coronovirusa"]
            d=random.choice(opcje)
            embed=discord.Embed(title=f"{member} {d}", color=0xE657EE)
            embed.set_image(url="https://1v1d1e1lmiki1lgcvx32p49h8fe-wpengine.netdna-ssl.com/wp-content/uploads/2020/03/virus-edm-corona-1-1-1.gif")
            await ctx.send(embed=embed)
        except:
            await ctx.send(traceback.format_exc())
        
def setup(bot):
    bot.add_cog(FunCog(bot))
    print('Fun Gotowe')


