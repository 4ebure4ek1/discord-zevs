a = ['Погода: пасмурная','Погода: ясная','Погода: грозовая','Погода: дождливая','Погода: ветренная','Погода: штормовая']
import random
import discord
from discord.ext import commands
from random import choice
from random import randint
import time

config = {
    'token': 'OTc4NzMyMTI5OTA1MTY4NDA1.GR8CzW.QQt5ELiTuMjd5kyc-qPzgNIVE4coxqZWMZ_bHQ',
    'prefix': '/',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def wt(ctx, *arg):
    await ctx.reply(random.randint(5, 50))
    await ctx.reply(random.choice(a))

    
bot.run(config['token'])
