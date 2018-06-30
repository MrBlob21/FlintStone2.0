```import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import pip
import random
from discord.ext import commands
import json
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),description="A Discord bot.\n\nHelp Commands",owner_id=435772465461854208)



@bot.command()
async def ping(ctx):
    """Premium ping pong giving you a websocket latency."""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Pong!')
    em.description = f"**{bot.latency * 1000:.4f} ms**"
    await ctx.send(embed=em)



if not os.environ.get('TOKEN'):
    print("ERROR: Bot token not found.")
bot.run(os.environ.get('TOKEN').strip('"'))```
