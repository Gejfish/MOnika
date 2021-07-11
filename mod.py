from discord import channel
from discord.ext import commands
import discord
import cogs
import random
import asyncio
import requests
from discord import File
import json
import os
import traceback
from discord import User
from discord.ext.commands import Bot

class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):            
        time = str(ctx.message.guild.created_at).split(" ")[0]
        osoby = ctx.guild.member_count
        guild_id = ctx.guild.id
        guild_owner = f"<@!{ctx.guild.owner_id}>"
        embed = discord.Embed(colour=0xE657EE)
        embed.set_author(name=f'Informacje o serwerze {ctx.guild}')
        embed.add_field(name='Właściciel:', value=guild_owner, inline=False)
        embed.add_field(name='Id servera:', value=guild_id, inline=False)
        embed.add_field(name='Ilość osób:', value=osoby, inline=False)
        embed.add_field(name='Ilość botów:', value="Idk", inline=False)
        embed.add_field(name='Ilość kanałów:', value=len(ctx.guild.channels), inline=False)
        embed.add_field(name='Ilość ról:', value=len(ctx.guild.roles), inline=False)
        embed.add_field(name='Ilość emotek:', value=len(ctx.guild.emojis), inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Serwer został stworzony dnia {time}')
    
        await ctx.send(embed=embed)

    @commands.command()
    async def servers(self, ctx):
        activeservers = self.bot.guilds
        if ctx.author.id == 453950321790550016:
            for guild in activeservers:
                await ctx.send(guild.name)
        if ctx.author.id == 327899255249436672:
            for guild in activeservers:
                await ctx.send(guild.name)
        if not ctx.author.id == 327899255249436672 or 453950321790550016:
            embed=discord.Embed(title="Nie ma tak łatwo chuju", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def kick(self, ctx, member : discord.Member=None, *, reason=None):
        if not member:
            embed=discord.Embed(title="Nie podałeś użytkownika", color=0xE657EE)
            await ctx.send(embed=embed)
        if ctx.author.top_role <= member.top_role:
           embed=discord.Embed(title="Brak permisji!", description=f"{ctx.author} Nie masz wystarczajocych permisji", color=0xE657EE)
           return await ctx.send(embed=embed)
        if ctx.author.guild_permissions.kick_members == True:
           await member.kick(reason=reason)
           embed=discord.Embed(title="Kick!", description=f"Wyrzucono użytkownika: {member} powód: `{reason}`.", color=0xE657EE)
           await member.kick(reason=reason)
           await ctx.send(embed=embed)
        if not ctx.author.guild_permissions.kick_members:
           embed=discord.Embed(title="Brak permisji!", description=f"{ctx.author} Nie masz wystarczających permisji", color=0xE657EE)
           await ctx.send(embed=embed)

    @commands.command()
    async def unban(self, ctx, *, member):
        if ctx.author.guild_permissions.ban_members == False: 
            e=discord.Embed(title="Nie posiadasz uprawnień aby odbanować użykownika", color=0xE657EE)
            return await ctx.send(embed=e)
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed=discord.Embed(title="Odbanowaleś", description=f"{user.mention} Uwu", color=0xE657EE)
                    await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="Nie posiadam uprawnien aby odbanowac", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def ban(self, ctx, member : discord.Member=None, *, reason=None):
        if not ctx.author.guild_permissions.ban_members:
            embed=discord.Embed(title="Brak permisji!", description=f"{ctx.author} Nie masz wystarczajocych permisji", color=0xE657EE)
            return await ctx.send(embed=embed)
        if not member:
            embed=discord.Embed(title="Nie podałeś użytkownika", color=0xE657EE)
            return await ctx.send(embed=embed)
        if ctx.author.top_role <= member.top_role:
            embed=discord.Embed(title="Brak permisji!", description=f"{ctx.author} Nie masz wystarczajocych permisji", color=0xE657EE)
            return await ctx.send(embed=embed)
        try:
            if ctx.author.guild_permissions.ban_members == True:
                await member.ban(reason=reason)
                embed=discord.Embed(title="Ban!", description=f"Zbanowano użytkownika powód: `{reason}`.", color=0xE657EE)
                await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="Nie posiadam uprawnień do banowania", color=0xE657EE)
            await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def giverole(self, ctx, user: discord.Member=None, role: discord.Role=None):
        if not user:
            embed=discord.Embed(title="Nie podałeś użytkownika", color=0xE657EE)
            return await ctx.send(embed=embed)
        if not role:
            embed=discord.Embed(title="Nie podałeś roli", color=0xE657EE)
            return await ctx.send(embed=embed)
        if not ctx.author.guild_permissions.administrator == True:
            embed=discord.Embed(title="Nie masz uprawnień", color=0xE657EE)
            await ctx.send(embed=embed)
        if ctx.author.guild_permissions.administrator == True:
            await user.add_roles(role)
            embed=discord.Embed(title="Dodałeś role:", description=f"{user.name} Dostał role {role.name}", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, m: discord.Member=None):
        if not m:
           m = ctx.author
        roles = [role for role in m.roles]
        embed = discord.Embed(colour=0xE657EE, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {m}")
        embed.set_thumbnail(url=m.avatar_url)
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID:", value=m.id)
        embed.add_field(name="Nazwa użytkownika na serwerze:", value=m.display_name)
        embed.add_field(name="Stworzone w:", value=m.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Dołączył w:", value=m.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Role ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role:", value=m.top_role.mention)
        embed.add_field(name="Bot?", value=m.bot)

        await ctx.send(embed=embed)

    @commands.command(aliases=['clean'])
    async def clear(self, ctx, *, arg):
        if ctx.author.guild_permissions.manage_messages == True:
            try:
                embed=discord.Embed(title=f"Usunaleś {int(arg)} wiadomości", color=0xE657EE)
                await ctx.send(embed=embed)
                await asyncio.sleep(0.5)
                await ctx.channel.purge(limit=int(arg) + 2)
            except ValueError:
                if arg == "w chuj":
                    embed=discord.Embed(title=f"Usunaleś w chuj wiadomosci czyli 100 wiadomości", color=0xE657EE)
                    await ctx.send(embed=embed)
                    await asyncio.sleep(0.5)
                    await ctx.channel.purge(limit=100 + 2)
                else:
                    e=discord.Embed(title="Argument nie jest liczba", color=0xE657EE)
                    await ctx.send(embed=e)
        if not ctx.author.guild_permissions.manage_messages:
            embed=discord.Embed(title="Nie masz permisji żeby usuwać wiadmości", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def mute(self, ctx, user: discord.Member=None, *, reason=None):
        if not user:
            a=discord.Embed(title="Nie podałeś użytkownika", color=0xE657EE)
            return await ctx.send(embed=a)
        
        if not ctx.author.guild_permissions.mute_members == True:
            embed=discord.Embed(title="Nie masz wystarczających premisji", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.top_role <= user.top_role:
                    embed=discord.Embed(title="Nie masz wystarczających premisji", color=0xE657EE)
                    return await ctx.send(embed=embed)
        try:
            for channel in ctx.guild.channels:
                overrite = channel.overwrites_for(user)
                overrite.update(send_messages=False, add_reactions=False)
                await channel.set_permissions(user, overwrite=overrite, reason=reason)
            e=discord.Embed(title=f"Zmutowano `{user.name}` przez `{ctx.author.name}`", color=0xE657EE)
            await ctx.send(embed=e)
        except:
            e=discord.Embed(title="Nie posiadam uprawnien aby go zmutowac", color=0xE657EE)
            await ctx.send(embed=e)

    @commands.command()
    async def unmute(self, ctx, user: discord.Member=None, *, reason=None):
        if not user:
            a=discord.Embed(title="Nie podałeś użytkownika", color=0xE657EE)
            return await ctx.send(embed=a)
        
        if not ctx.author.guild_permissions.mute_members == True:
            embed=discord.Embed(title="Nie masz wystarczających premisji", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.top_role <= user.top_role:
            embed=discord.Embed(title="Nie masz wystarczających premisji", color=0xE657EE)
            return await ctx.send(embed=embed)
        
        
        try:
            for channel in ctx.guild.channels:
                overrite = channel.overwrites_for(user)
                overrite.update(send_messages=None, add_reactions=None)
                empty = overrite.is_empty()
                if empty:
                    await channel.set_permissions(user, overwrite=None, reason=reason)
                else:
                    await channel.set_permissions(user, overwrite=overrite, reason=reason)
            e=discord.Embed(title=f"Odmutowano `{user.name}` przez `{ctx.author.name}`", color=0xE657EE)
            await ctx.send(embed=e)
        except:
            e=discord.Embed(title="Nie posiadam uprawnien aby go odmutowac", color=0xE657EE)
            await ctx.send(embed=e)

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason="nie podano powodu"):

        if ctx.author.guild_permissions.kick_members == False:
            embed=discord.Embed(title="Nie masz permisji aby dawać warny", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.top_role <= member.top_role:
            embed=discord.Embed(title="Nie możesz dać warna tej osobie", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.guild_permissions.kick_members == True:
            with open("warns.json", "r") as f:
                warns = json.load(f)
                if not str(ctx.guild.id) in warns:
                    warns[str(ctx.guild.id)] = {}

                if not str(member.id) in warns[str(ctx.guild.id)]:
                    warns[str(ctx.guild.id)][str(member.id)] = {}

                warns[str(ctx.guild.id)][str(member.id)][str(len(warns[str(ctx.guild.id)][str(member.id)]) + 1)] = reason

            with open("warns.json", "w") as f:
                json.dump(warns, f, indent=4)

            embed=discord.Embed(title=f"`{member.name}` dostał ostrzeżenie z powodu `{reason}`", color=0xE657EE)
            e=discord.Embed(title=f"Dostałeś ostrzeżenie przez `{ctx.author.name}` na serwerze `{ctx.guild.name}` z powodu `{reason}`", color=0xE657EE)
            await ctx.send(embed=embed)
            await member.send(embed=e)

    @commands.command()
    async def warns(self, ctx, member: discord.Member=None):
          
        member = member or ctx.author
        
        with open("warns.json", "r") as f:
            warns = json.load(f)

        e = discord.Embed(title=f"Warny użytkownika {member.name}:", description="\n".join([f"{warn}. {warns[str(ctx.guild.id)][str(member.id)][warn]}" for warn in warns[str(ctx.guild.id)][str(member.id)]]), color=0xE657EE)
        await ctx.send(embed=e)

    @commands.command()
    async def removewarn(self, ctx, member: discord.Member, _id: str):

        if ctx.author.guild_permissions.kick_members == False:
            embed=discord.Embed(title="Nie masz permisji aby dawać warny", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.top_role <= member.top_role:
            embed=discord.Embed(title="Nie możesz dać warna tej osobie", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.guild_permissions.kick_members == True:
            with open("warns.json", "r") as f:
                warns = json.load(f)
                del warns[str(ctx.guild.id)][str(member.id)][_id]

            with open("warns.json", "w") as f:
                json.dump(warns, f, indent=4)
            
            embed=discord.Embed(title=f"Usunięto warna o ID `{_id}` użytkownikowi `{member.name}`", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def clearwarns(self, ctx, member: discord.Member):

        if ctx.author.guild_permissions.kick_members == False:
            embed=discord.Embed(title="Nie masz permisji aby dawać warny", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.top_role <= member.top_role:
            embed=discord.Embed(title="Nie możesz dać warna tej osobie", color=0xE657EE)
            return await ctx.send(embed=embed)

        if ctx.author.guild_permissions.kick_members == True:  
            with open("warns.json", "r") as f:
                warns = json.load(f)
                del warns[str(ctx.guild.id)][str(member.id)]

            with open("warns.json", "w") as f:
                json.dump(warns, f, indent=4)
            
            embed=discord.Embed(title=f"Użytkownik `{member.name}` został wyczyszczony z warnów", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command()
    async def addtodo(self, ctx, *, arg):
        arg = arg.replace("@", "@\u200b")
        if len(arg) > 100:
           return await ctx.send("Wiadomość przekroczyła limit znaków (`limit 100`)")

        with open("todo.json", "r") as f:
            t = json.load(f)
        if not str(ctx.author.id) in t:
            t[str(ctx.author.id)] = "Lista rzeczy do zrobienia:"
            
        t[str(ctx.author.id)] = t[str(ctx.author.id)] + "\n- " + arg

        with open("todo.json", "w") as f:
           json.dump(t, f, indent=4)
        embed=discord.Embed(title=f"Dodano `{arg}` do twojego todo", color=0xE657EE)
        await ctx.send(embed=embed)

    @commands.command()
    async def cleartodo(self, ctx):
        with open("todo.json", "r") as f:
           iu = json.load(f)
           iu[str(ctx.author.id)] = "Lista rzeczy do zrobienia:"

        with open("todo.json", "w") as f:
           json.dump(iu, f, indent=4)

        embed=discord.Embed(title="Wyczyszczono twoje todo", color=0xE657EE)
        await ctx.send(embed=embed)

    @commands.command(description="Usuwa tekst z todo", usage="todo remove (tekst)", aliases=["-", "delete", "rem", "del"])
    async def removetodo(self, ctx, *, arg):
        arg = arg.replace("@", "@\u200b")
        with open("todo.json", "r") as f:
           t = json.load(f)

           t[str(ctx.author.id)] = t[str(ctx.author.id)].replace("\n- " + arg, "")

        with open("todo.json", "w") as f:
           json.dump(t, f, indent=4)

        embed=discord.Embed(title=f"Usunięto `{arg}` z todo.")
        await ctx.send(embed=embed)

    @commands.command()
    async def viewtodo(self, ctx, member: discord.Member=None, m: discord.Member=None):
        try:
            m = member or ctx.author
            if not member:
                with open("todo.json", "r") as f:
                    iu = json.load(f)

                if str(ctx.author.id) not in iu:
                    ius = "Użytkownik nie posiada todo :C"
                else:
                    ius = iu[str(ctx.author.id)]
                        
                    e=discord.Embed(title=f"Todo użytkownika {ctx.author.name}", description=ius, colour=0xE657EE)
                    e.set_thumbnail(url=(m.avatar_url))

                    return await ctx.send(embed=e)

            with open("todo.json", "r") as f:
                iu = json.load(f)

            if str(member.id) not in iu:
                ius = "Użytkownik nie posiada todo :C"
            else:
                ius = iu[str(member.id)]

            e=discord.Embed(title=f"Todo użytkownika {member.name}", description=ius, colour=0xE657EE, timestamp=ctx.message.created_at)
            e.set_thumbnail(url=(m.avatar_url))

            await ctx.send(embed=e)
        except:
            await ctx.send(traceback.format_exc())

def setup(bot):
    bot.add_cog(ModCog(bot))
    print('Mod Gotowe')
