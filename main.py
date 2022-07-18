import discord
import os
import json
import asyncio
import argparse
import time
import requests
import discord.ext
from os import getenv
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check


client = discord.Client()
parser = argparse.ArgumentParser()
client = commands.Bot(command_prefix = '') #here is where we will put our bots prefix 



#####################################################################################################################################################################
##                                                                     IP Command                                                                                  ##
#####################################################################################################################################################################

@client.command()
async def ip(ctx): #the command will be ip
    await ctx.send('The Server IP Is outbackroleplay.cf:10527, Join By Searching Outback Roleplay or By Pressing F8 Than Typing connect outbackroleplay.cf:10527') #Here You Can Put Your Ip So Users Can Easily Access your server.

#####################################################################################################################################################################
##                                                                      Embeds                                                                                     ##
#####################################################################################################################################################################
#This Embed Will Be For Your Info 
@client.command()
async def infoembed(ctx): #the command will be infoembed
    embed=discord.Embed(title="**Outback Roleplay Server Info**", description="Welcome to ORP, We are a privately owned FiveM server based off of the wonderful state of Blaine County. Our goal is to bring unique and the most Realistic RP scenarios different than any other server out there. Quote that the server is still being developed, We will still have active patrols every night with averaging up to 13 people, What makes our server so unique is the custom vehicles we have to offer, We offer over 400+ custom free vehicles for everyone to use! We also ensure users the MAX performance as we run off of extreme hardware.", color=0x00ff00) 
    #First Info Field
    embed.add_field(name="**Discord Link**", value="https://discord.gg/6jrkyqBrzF", inline=False)
#Second Info Field
    embed.add_field(name="**Server IP**", value="The Server IP Is outbackroleplay.cf:10527", inline=False)
#Third Info Field
    embed.add_field(name="**Cad Link**", value="The Cad Invite Link Is https://www.adrencad.com/invite/1XWu87WR", inline=False)
#Fourth Info Field
    embed.add_field(name="**Store Link**", value="The Store Link Is storeLink.var=UNDEFINED", inline=False)
#Fifth Info Field
    embed.add_field(name="**Applications**", value="You Can Find The Applications In <#995196668666450012>", inline=False)
#Sixth Info Field
    embed.add_field(name="**Server Rules**", value="You Can Find The Server Rules In <#995196590161661973>", inline=False)
#Credits/Footer
    embed.set_footer(text="Coded By CommandX (CommandX#5389)")
    await ctx.send(embed=embed)
#####################################################################################################################################################################
##                                                                      Status                                                                                     ##
#####################################################################################################################################################################
parser.add_argument(
	'--server', 
	'-S',
	type=str, 
	required=False,
	default='outbackroleplay.cf', #Change To Your Server IP
	help="outbackroleplay.cf" #Change To Your Server IP
)

parser.add_argument(
	'--port', 
	'-P',
	type=str, 
	required=False,
	default='10527', #Change To Your Server Port
	help="10527" #Change To Your Server Port
)

parser.add_argument(
	'--timeout', 
	'-T',
	type=int, 
	required=False,
	default='10', #Change To How Often In seconds you want it to update
	help="10" #Change To How Often In seconds you want it to update
)

parser.add_argument(
	'--players', 
	'-Pc',
	type=int, 
	required=False,
	default='32', #Change To The Max Amount Of Players than can join your server
	help="32" #Change To The Max Amount Of Players than can join your server
)

arguments = parser.parse_args()
server_endpoint = f'http://{arguments.server}:{arguments.port}/players.json'

if getenv("DISCORDM") is not None:
	pass
else:
	exit("[!] DISCORDM environment variable has not been set.")

# Iterate over JSON array and parse the count of all players.
def onlinePlayers():
	try:
		while(True):
			try:
				response = requests.get(server_endpoint, timeout=5).json()
			except:
				print(f"[!] Error. Requesting {server_endpoint}. Check your connection.")
				exit(0)

			online_players = []

			for player in response:
				online_players.append(player['name'])
			
			return online_players
	except:
		exit()

@client.event
async def on_ready():
		print("[*] Bot is running!\n")
		print("[*] Authenticated as:" , client.user, end='\n\n')
		await client.change_presence(activity=discord.Game(name='Loading..'))

async def change():
	await client.wait_until_ready()
	while not client.is_closed():
		serverData = onlinePlayers()
		currentOnline = len(serverData)
		currentStatus = 'Online: {}/{}'.format(str(currentOnline), str(arguments.players))

		print("[*] Total Player(s):", str(currentOnline), end='\n\n')

		index = 1
		for player in serverData:
			print(str(index) + ":" + player)
			index += 1
		
		await client.change_presence(activity=discord.Game(name=currentStatus))
		await asyncio.sleep(arguments.timeout)

try:
	client.loop.create_task(change())
	time.sleep(1)
	client.run(getenv('DISCORDM'))
	
except discord.errors.LoginFailure:
	exit('Error. Invalid Token. Please Verify and try again.')








#####################################################################################################################################################################

#All Coded By CommandX, Message @CommandX#5389 on discord for support.

#I know this is a simple bot, But Im new to discord.py, This is something "big" for me, I will be adding more soon, DM me suggestions, Thank You For Using This Bot!
