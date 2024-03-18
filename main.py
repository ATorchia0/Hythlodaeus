# This example requires the 'message_content' intent.

import discord
from discord.ext import commands, tasks
from ffxiv import *
from holiday import *
import datetime

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

#time the message will send
#utc is default #10AM EST
messageTime = datetime.time(hour=14) 
#method to send all the holidays in discord channel at the specified time
@tasks.loop(time=messageTime)
async def NationalDaySend():
    channel = bot.get_channel(int(CHANNEL)) #this is where the channel id should go!!!
    days = updateHolidays()
    embed = discord.Embed(title="Here Are The Fun Holidays For Today")
    for holiday in days:
        embed.add_field(name='\n', value=f'{holiday}\n', inline=False)
    await channel.send(embed=embed)

bot.run('KEYGOESHERE')
