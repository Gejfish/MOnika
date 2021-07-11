from discord.ext import commands
import discord
import cogs
import asyncio
import os

bot = commands.Bot(command_prefix="$")

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "<@!707952241536925736>":
           embed = discord.Embed(title='Moja główna komenda to $komendy', color=0xE657EE)
           await message.channel.send(embed=embed)
            
def setup(bot):
    bot.add_cog(PingCog(bot))
    print('Ping Gotowe')