import ast
import discord
from discord.ext import commands
import json
import asyncio

bot = commands.Bot(command_prefix='$', description='Najlepszy bot na świecie bez kappy.')

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)
        
class Developerskie(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def eval(self, ctx, *, cmd):
        if ctx.author.id == 453950321790550016:
            try:
                fn_name = "_eval_expr"

                cmd = cmd.strip("` ")

                cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

                body = f"async def {fn_name}():\n{cmd}"

                parsed = ast.parse(body)
                body = parsed.body[0].body

                insert_returns(body)

                env = {
                    'bot': ctx.bot,
                    'discord': discord,
                    'commands': commands,
                    'ctx': ctx,
                    '__import__': __import__
                }

                exec(compile(parsed, filename="<ast>", mode="exec"), env)

                result = (await eval(f"{fn_name}()", env))
                msg = await ctx.send(result)
            except Exception as e:
                msg = await ctx.send(f"```{e}```")
                
            def check(r, m):
                return m == ctx.author and str(r.emoji) == "⏹️" and r.message.id == msg.id
            try:
                await self.bot.wait_for("reaction_add", check=check, timeout=120)
                return await msg.delete()
            except:
                return

        if ctx.author.id == 327899255249436672:
            try:
                fn_name = "_eval_expr"

                cmd = cmd.strip("` ")

                cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

                body = f"async def {fn_name}():\n{cmd}"

                parsed = ast.parse(body)
                body = parsed.body[0].body

                insert_returns(body)

                env = {
                    'bot': ctx.bot,
                    'discord': discord,
                    'commands': commands,
                    'ctx': ctx,
                    '__import__': __import__
                }

                exec(compile(parsed, filename="<ast>", mode="exec"), env)

                result = (await eval(f"{fn_name}()", env))
                msg = await ctx.send(result)
            except Exception as e:
                msg = await ctx.send(f"```{e}```")
                
            def check(r, m):
                return m == ctx.author and str(r.emoji) == "⏹️" and r.message.id == msg.id
            try:
                await self.bot.wait_for("reaction_add", check=check, timeout=120)
                return await msg.delete()
            except:
                return
          
        
        else:
            e = discord.Embed(title="Nie masz uprawnień", color=0xE657EE)
        await ctx.send(embed=e)

def setup(client):
    client.add_cog(Developerskie(bot))
    print("Załadowano developerskie")