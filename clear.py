import os
import discord
from discord.ext import commands
import requests
import json
import time


token = ""
prefix = '!'

bot = commands.Bot(command_prefix="",
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    activity = discord.Game(name="clearing messages")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print('-' * 30)
    print('Logged in as: ')
    print(bot.user)
    print('-' * 30)


@bot.event
async def on_message(message):
    channel = message.channel
    if message.author == bot.user:
        if message.content.startswith(prefix + "clear"):
            async for msg in channel.history(limit=9999):
                try:
                  await msg.delete()
                  time.sleep(1)
                except Exception as x:
                    pass
        if message.content.startswith(prefix + "cleardms"):
            for channel in bot.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == bot.user:
                                await msg.delete()
                                time.sleep(1)
                        except:
                             pass
        if message.content.startswith(prefix + "clearthis"):
            if isinstance(channel, discord.DMChannel):
                async for msg in channel.history(limit=9999):
                    try:
                        if msg.author == bot.user:
                            await msg.delete()
                            time.sleep(1)
                    except:
                         pass


bot.run(token)
