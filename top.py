import topgg
import discord
from discord.ext import commands


class top(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcwNzk1MjI0MTUzNjkyNTczNiIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA4NDg0NzQwfQ.JvqYqofZpcuUSrLrTsLhRllvxh0nYUdbp0-wtDbNDzo" # set this to your DBL token
        self.topgg = topgg.DBLClient(self.bot, self.token, autopost=True) # Autopost will post your guild count every 30 minutes

    async def on_guild_post():
        print("Server count posted successfully")

def setup(bot):
    bot.add_cog(top(bot))