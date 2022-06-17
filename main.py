import discord
import requests
import json

#add your token here
TOKEN = ""


client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message} ({channel})")
  if message.author == client.user:
    return
    #this bot works only for this specific channel, you can change this line
  if message.channel.name == "facts": 
    if user_message.lower() == "!catfact":
      #getting random facts from api  
      response = requests.get("https://catfact.ninja/fact")
      fact = response.json()
      await message.channel.send(fact['fact'])
      return


client.run(TOKEN)