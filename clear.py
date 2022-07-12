import discord, asyncio, time

client = discord.Client()

token = ""
prefix = '!'

@client.event
async def on_ready():
    activity = discord.Game(name="clearing messages")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print('-' * 30)
    print('Logged in as: ')
    print(client.user)
    print('-' * 30)


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        if message.content.startswith(prefix + "clear"):
            async for msg in channel.history(limit=9999):
                try:
                  await msg.delete()
                  time.sleep(1)
                except Exception as x:
                    pass
        if message.content.startswith(prefix + "cleardms"):
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                time.sleep(1)
                        except:
                             pass
        if message.content.startswith(prefix + "clearthis"):
            if isinstance(channel, discord.DMChannel):
                async for msg in channel.history(limit=9999):
                    try:
                        if msg.author == client.user:
                            await msg.delete()
                            time.sleep(1)
                    except:
                         pass

client.run(token, bot=False)
