import discord
from discord.ext import commands
import traceback


class Komendy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def komendyddlc(self, ctx):
        embed = discord.Embed(title="Komendy o doki doki literature club", description="Lista komend o doki doki literature club:", color=0xE657EE)
    
        embed.add_field(name="$infomonika", value="Informacje o Monice", inline=False)
        embed.add_field(name="$infoyuri", value="Informacje o Yuri", inline=False)
        embed.add_field(name="$infosayori", value="Informacje o Sayori", inline=False)
        embed.add_field(name="$infonatsuki", value="Informacje o Natsuki", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def komendyzabawne(self, ctx):
        embed = discord.Embed(title="Komendy zabawne", description="Lista komend zabawnych:", color=0xE657EE)
    
        embed.add_field(name="$cat", value="Wysyła zdjęcia kotów :cat:", inline=True)
        embed.add_field(name="$redpanda", value="Wysyła zdjęcia czerwonych pand", inline=True)
        embed.add_field(name="$panda", value="Wysyła zdjęcia pand", inline=True)
        embed.add_field(name="$dog", value="Wysyła zdjęcia psów :dog:", inline=True)
        embed.add_field(name="$anime", value="Wysyła zdjęcia postaci z anime UwU", inline=True)
        embed.add_field(name="$avatar (kto)", value="Pokazuje avatar użytkownika", inline=True)
        embed.add_field(name="$randomn (od, do)", value="Losowa liczba", inline=True)
        embed.add_field(name="$ideologia", value="Losuje ideologie", inline=True)
        embed.add_field(name="$religia", value="Losuje religie", inline=True)
        embed.add_field(name="$8ball (pytanie)", value="Opowiedź na każde pytanie", inline=True)
        embed.add_field(name="$ping", value="Pokazuje ping bota", inline=True)
        embed.add_field(name="$countryroulet", value="Losowy kraj", inline=True)
        embed.add_field(name="$pat (kto)", value="Pogłaskał kogoś po głowie", inline=True)
        embed.add_field(name="$feed (kto)", value="Nakarm kogoś", inline=True)
        embed.add_field(name="$chucknorris", value="Żarty o chucknorrisie w różnych językach", inline=True)
        embed.add_field(name="$hug (kto)", value="Przytulasz wybraną osobe :3", inline=True)
        embed.add_field(name="$kiss (kto)", value="Całujesz wybraną osobe :3", inline=True)
        embed.add_field(name="$howhomo (kto)", value="Sprawdza kto w ilu % jest homo", inline=True)
        embed.add_field(name="$slap (kto)", value="Uderzasz wybraną osobe >M<", inline=True)
        embed.add_field(name="$legia", value="Okazja do odjebania niezlego buntu", inline=True)
        embed.add_field(name="$say (co)", value="Bot wysyła wiadomość", inline=True)
        embed.add_field(name="$esay (co)", value="Bot wysyła wiadomość w embedzie", inline=True)
        embed.add_field(name="$trigger", value="Bot wysyła triggered profilowe", inline=True)
        embed.add_field(name="$losowanie (co) (co)", value="Wysyła randomowe słowo ktore podasz", inline=True)

        e=discord.Embed(title="Komendy zabawne", description="Lista komend zabawnych część 2", color=0xE657EE)
        e.add_field(name="$youtube (co)", value="Wyszukuje na youtubie", inline=True)
        e.add_field(name="$google (co)", value="Wyszukuje w google", inline=True)
        e.add_field(name='$pogoda (miasto)', value='Podaje pogode w podanym miescie', inline=True)
        e.add_field(name='$beautiful (kto)', value='Wysyla beautiful meme', inline=True)
        e.add_field(name='$servericon', value='Wysyla ikone servera', inline=True)
        e.add_field(name='$twitch (co)', value='Wyszukuje dane slowa w twitchu', inline=True)
        e.add_field(name='$worsethan (kto)', value='Gorsze niz hitler meme', inline=True)
        e.add_field(name='$neko', value='Wysyla anime koty', inline=True)
        e.add_field(name='$coronovirus (kto)', value='Sprwadza czy ma coronovirusa', inline=True)
        e.add_field(name='$memy', value='Wysyla memy z Jeb z dzidy', inline=True)

        await ctx.send(embed=embed)
        await ctx.send(embed=e)

    @commands.command()
    async def komendylvl(self, ctx):
        embed = discord.Embed(title="$Komendylvl", description="Komendy do lvlów", color=0xE657EE)
        embed.add_field(name="$level", value="Pokazuje aktualny lvl", inline=False) 
        embed.add_field(name="$lvlon", value="Włącza wiadmość o nowym lvlu", inline=False)
        embed.add_field(name="$lvloff", value="Wyłącza wiadomość o nowym lvlu", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def komendy(self, ctx):
        embed = discord.Embed(title="Komendy", description="Lista komend bota:", color=0xE657EE)
     
        embed.add_field(name="Prefix", value="$", inline=False)
        embed.add_field(name="$komendyzabawne", value="Lista zabawnych komend", inline=False)
        embed.add_field(name="$komendymatematyczne", value="Lista komend matematycznych", inline=False)
        embed.add_field(name="$komendymoderacyjne", value="Lista komend moderacyjncyh", inline=False) 
        embed.add_field(name="$komendyddlc", value="Lista komend o doki doki literature club", inline=False)
        embed.add_field(name="$komendytodo", value="Lista komend do todo", inline=False)
        embed.add_field(name="$komendylvl", value="Lista komend do lvlów", inline=False)
        embed.add_field(name="$komendymuzyczne", value="Lista komend muzycznych", inline=False)
        embed.add_field(name="$komendy", value="Lista komend", inline=False)
        embed.add_field(name="$info", value="Informacje o bocie", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def komendymatematyczne(self, ctx):
        embed = discord.Embed(title="Komendy matematyczne", description="Lista komend matematycznych:", color=0xE657EE)
    
        embed.add_field(name="$add (liczby)", value="Dodawanie dwóch liczb", inline=False)
        embed.add_field(name="$multiply (liczby)", value="Mnożenie dwóch liczb", inline=False)
        embed.add_field(name="$split (liczby)", value="Dzielenie dwóch liczb", inline=False)
        embed.add_field(name="$remove (liczby)", value="Odejmowanie dwóch liczb", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def komendymoderacyjne(self, ctx):
        embed = discord.Embed(title="Komendy moderacyjne", description="Lista komend moderacyjnych:", color=0xE657EE)
    
        embed.add_field(name="$kick (kto) (powod)", value="Wyrzuca użytkownika z serwera", inline=False)
        embed.add_field(name="$ban (kto) (powod)", value="Banuje użytkownika z serwera", inline=False)
        embed.add_field(name="$clear (ilość) ", value="Usuwa wybraną ilość wiadomości", inline=False)
        embed.add_field(name="$userinfo (kto)", value="Pokazuje informacje o użytkowniku", inline=False)
        embed.add_field(name="$giverole (@komu) (@rola)", value="Daje range użytkowikowi", inline=False)
        embed.add_field(name="$warn (@komu) (powód) ", value="Daje warna użytkownikowi", inline=False)
        embed.add_field(name="$poll (Tresc)", value="Tworzy ankiete", inline=False)
        embed.add_field(name="$warns (@komu)", value="Sprawdza warny", inline=False)
        embed.add_field(name="$removewarn (@komu) (jaki)", value="Usuwa warna", inline=False)
        embed.add_field(name="$clearwarns (@komu)", value="Usuwa wszystkie warny użytkowinkowi", inline=False)
        embed.add_field(name="$unmute (kogo)", value="Unmutje uzytkownika (jezeli jego rola nie posiada admina)", inline=False)
        embed.add_field(name="$mute (kogo)", value="Wycisza uzytkownika (jezeli jego rola nie posiada admina)", inline=False)
        e=discord.Embed(title="Komendy moderacyjne część 2", color=0xE657EE)

        await ctx.send(embed=embed)

    @commands.command()
    async def komendytodo(self, ctx):
        embed = discord.Embed(title="Komendy todo", description="Lista komend todo:", color=0xE657EE)
    
        embed.add_field(name="$viewtodo (osoba)", value="Pokazuje todo", inline=False)
        embed.add_field(name="$cleartodo", value="Czyści todo", inline=False)
        embed.add_field(name="$addtodo (co)", value="Dodaje do todo", inline=False)
        embed.add_field(name="$removetodo (co)", value="Usuwa z todo", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def komendymuzyczne(self, ctx):
            embed = discord.Embed(title="Komendy muzyczne", description="Lista komend muzycznych:", color=0xE657EE)

            embed.add_field(name="$join", value="Dołączam na kanał głosowy", inline=False)
            embed.add_field(name="$leave", value="Rozłączam się z kanału głosowego", inline=False)
            embed.add_field(name="$play (nazwa piosenki)", value="Gram wybraną piosenke", inline=False)
            embed.add_field(name="$skip", value="Zmieniam piosenke na następną", inline=False)
            embed.add_field(name="$queue", value="Wyświetla kolejke piosenek", inline=False)
            embed.add_field(name="$now", value="Pokazuje aktulanie graną piosenke", inline=False)
            embed.add_field(name="$volume", value="Zmienia głośność", inline=False)
            embed.add_field(name="$loop", value="Loopuje piosenke", inline=False)
            embed.add_field(name="$stop", value="Czysci kolejke i zatrzymuje odtwarzanie muzyki", inline=False)
            embed.add_field(name="$pause", value="Zatrzymuje piosenke", inline=False)
            embed.add_field(name="$shuffle", value="Miesza kolejke piosenek", inline=False)
            embed.add_field(name="$lyrics (jaka piosenka)", value="Tekst piosenki", inline=False)

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Komendy(bot))
    print("Załadowano komendy pomocne")
