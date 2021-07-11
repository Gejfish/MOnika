import discord
from discord.ext import commands
import traceback

class ErrorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)

        print(traceback.format_exc())
         
        if isinstance(error, commands.CommandNotFound):
            embed=discord.Embed(title="Nie znaleziono takiej komendy sprawdź $komendy", color=0xE657EE)
            embed.set_image(url="https://media1.tenor.com/images/d22f943bb7e00e95b9669ac4ee0de608/tenor.gif?itemid=15633073")
            return await ctx.send(embed=embed)
                 
def setup(bot):
    bot.add_cog(ErrorCog(bot))
    print("Errory Gotowe")