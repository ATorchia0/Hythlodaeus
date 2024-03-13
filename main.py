# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from ffxiv import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.hybrid_command()
async def nextmaint(ctx):
    """
Checks to see when the next loadstone maintenance is.
"""
    maint = getMaintStatus()
    if(maint == 0):
        msg = 'No Known Maintenances Exist'
    else:
        msg = getMaintURL()
    await ctx.send(msg)
    
@bot.command()
async def treeSync(ctx):
    await bot.tree.sync()
    print(bot.tree)

bot.run('KEYGOESHERE')
