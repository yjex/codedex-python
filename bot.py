# requests package allows making HTTP requests to any url
import requests
# allows reading of JSON data
import json
import discord
import env

# using GET method to URL giving meme data
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())

# sets the intents passed into given instance of MyClient (settings for what Discord bot can access)
# default() behaviour assigned
intents = discord.Intents.default()
# explicitly allowing the bot to interact with messages
intents.message_content = True

# initiates MyClient class, calls run (main way to start the client)
# client uses token to authenticate itself to the Discord backend servers 
client = MyClient(intents=intents)
client.run(env.token)

