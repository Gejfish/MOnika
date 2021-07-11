import discord
from discord.ext import commands
import json
import cogs

class LvlsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return
            
        with open("checkguildlvl.json", "r") as f:
            cg = json.load(f)

            if not str(msg.guild.id) in cg:
                checkguild = "off"
            else:
                checkguild = cg[str(msg.guild.id)]

        with open("osoby.json", "r") as f:
            lvl = json.load(f)

            if not str(msg.guild.id) in lvl:
                lvl[str(msg.guild.id)] = {}

            if not str(msg.author.id) in lvl[str(msg.guild.id)]:
                lvl[str(msg.guild.id)][str(msg.author.id)] = {}
                lvl[str(msg.guild.id)][str(msg.author.id)]["level"] = 1
                lvl[str(msg.guild.id)][str(msg.author.id)]["exp"] = 0

            lvl[str(msg.guild.id)][str(msg.author.id)]["exp"] = lvl[str(msg.guild.id)][str(msg.author.id)]["exp"] + 1

            if lvl[str(msg.guild.id)][str(msg.author.id)]["exp"] > lvl[str(msg.guild.id)][str(msg.author.id)]["level"] * 100:
                lvl[str(msg.guild.id)][str(msg.author.id)]["level"] = lvl[str(msg.guild.id)][str(msg.author.id)]["level"] + 1
                lvl[str(msg.guild.id)][str(msg.author.id)]["exp"] = 0
                if checkguild == "on":
                    embed=discord.Embed(title=f"{msg.author.name} zdobyłeś(-aś) `{lvl[str(msg.guild.id)][str(msg.author.id)]['level']}` level!",color=0xE657EE)
                    obrazek = "https://media.discordapp.net/attachments/671813538624569364/776107247738159144/pngwing.com.png"
                    embed.set_image(url=(obrazek))
                    await msg.channel.send(embed=embed)

        with open("osoby.json", "w") as f:
            json.dump(lvl, f, indent=4)

    @commands.command(aliases=["lvl"])
    async def level(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author

        with open("osoby.json", "r") as f:
            lvl = json.load(f)

            exp = lvl[str(ctx.guild.id)][str(member.id)]["exp"]
            level = lvl[str(ctx.guild.id)][str(member.id)]["level"]

        e = discord.Embed(title=f"Levele użytkownika {member.name}:", description=f"**Serwerowy level:**\nLevel: `{level}`\nExp: `{exp}` / `{level * 100}`", color=0xE657EE)
        e.set_thumbnail(url=str(member.avatar_url))

        await ctx.send(embed=e)
        
    @commands.command()
    async def komendaboska(self, ctx, member: discord.Member=None):  
        if ctx.author.id == 453950321790550016:
           with open("vips.json", "r") as f:
               vip = json.load(f)

               vip[str(member.id)] = "yes"

               with open("vips.json", "w") as f:
                   json.dump(vip, f, indent=4)

               embed=discord.Embed(title="Osoba zostala vipem", color=0xE657EE)
               await ctx.send(embed=embed)

        if ctx.author.id == 327899255249436672:
            with open("vips.json", "r") as f:
               vip = json.load(f)

               vip[str(member.id)] = "yes"

               with open("vips.json", "w") as f:
                   json.dump(vip, f, indent=4)

               embed=discord.Embed(title="Osoba zostala vipem", color=0xE657EE)
               await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="nie masz uprawnien", color=0xE657EE)
            await ctx.send(embed=embed)

    @commands.command(description="Włącza wiadomość po zdobyciu nowego levelu", usage="lvlon")
    async def lvlon(self, ctx):          
        with open("checkguildlvl.json", "r") as f:
            lvl = json.load(f)

            lvl[str(ctx.guild.id)] = "on"

        with open("checkguildlvl.json", "w") as f:
            json.dump(lvl, f, indent=4)

        embed=discord.Embed(title="Wiadmości o nowych lvlach zostały włączone", color=0xE657EE)
        await ctx.send(embed=embed)

    @commands.command()
    async def lvloff(self, ctx):
        with open("checkguildlvl.json", "r") as f:
            lvl = json.load(f)

            lvl[str(ctx.guild.id)] = "off"

        with open("checkguildlvl.json", "w") as f:
            json.dump(lvl, f, indent=4)

        embed=discord.Embed(title="Wiadmości o nowych lvlach zostały wylączone", color=0xE657EE)
        await ctx.send(embed=embed)
        
    @commands.command(aliases=["lvls"])
    async def chujciwcycycejebanapizdoitakniktniewpiszeczegostakiegotakzewyjebane(self, ctx):       
        with open("osoby.json", "r") as f:
            lvl = json.load(f)
            
            e = discord.Embed(title="Levele:", description="\n".join([f"{m.name} : `{lvl[str(ctx.guild.id)][str(m.id)]['level']}` (`{lvl[str(ctx.guild.id)][str(m.id)]['exp']}` / `{lvl[str(ctx.guild.id)][str(m.id)]['level'] * 100}`)" for m in [self.bot.get_user(int(m)) for m in lvl[str(ctx.guild.id)] if lvl[str(ctx.guild.id)][m]["level"] > 1 if m in [str(i.id) for i in ctx.guild.members]]]), color=0xE657EE)

            await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(LvlsCog(bot))