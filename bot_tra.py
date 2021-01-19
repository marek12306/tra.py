#!/usr/bin/env python3
import discord
import requests
import random
import imghdr
import io

trapy = ['astolfo_(fate)','astolfo','felix_argyle']

class Trapy(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        s = message.content.strip()
        if 'trapy' in s or 'tra.py' in s:
            r = requests.get('https://cure.ninja/booru/api/json?q={}+trap&f={}&o=r&s=1'.format(random.choice(trapy), 'e' if message.channel.is_nsfw() else 's'))
            url = r.json()['results'][0]['url']
            image = io.BytesIO(requests.get(url).content)
            imgformat = imghdr.what(image)
            await message.reply(file=discord.File(image, filename=f'trap.{imgformat}'))

client = Trapy()

client.run(open('.token', 'r').read())