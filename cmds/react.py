import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from core.classes import Cog_Extension

load_dotenv()
email = os.getenv('email')
password = os.getenv('password')


class React(Cog_Extension):

    @commands.command()
    async def start(self, ctx, map):
        if(map == "benchmark2"):
            await ctx.send("Start Benchmark2 map")
        else:
            await ctx.send("Error")

    @commands.command()
    async def status(self, ctx, map):
        if(map == "benchmark2"):
            await ctx.send("Benchmark2 Status")
        else:
            await ctx.send("Error")

    @commands.command()
    async def stop(self, ctx, map):
        if(map == "benchmark2"):
            await ctx.send("Stop Benchmark2 map")
        else:
            await ctx.send("Error")


def setup(bot):
    bot.add_cog(React(bot))
