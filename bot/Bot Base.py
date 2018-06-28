# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:04:56 2018

@author: Satan
"""
import os
from discord import Game
import discord
import random
from discord.ext.commands import Bot



os.chdir('C:\\Users\\Satan\\Desktop\\bot')

BOT_Prefix = ("?", "!")
Token = '''NDU2ODcwNjUyNzMzOTQ3OTE1.DgRExQ.D9MT5B1iROZgTil7zp0ary-zDCc'''

client = Bot(command_prefix = BOT_Prefix)


CurrentHate = []
with open(r"C:\Users\Satan\Desktop\bot\Responses.txt", 'r') as filehandle:
    for line in filehandle:
    
        ReadHate = line
        CurrentHate.append(ReadHate)

def Addhate(add):
    with open(r"C:\Users\Satan\Desktop\bot\Responses.txt", "a") as filehandle:
        filehandle.write("\n" + add)
    

@client.command(name = 'AddHate',   
                pass_context = True)
async def addHate(Hate):
    global add
    add = Hate

    
    global CurrentHate
    await client.say('Here is your Current Hate')
#tell usere the hate
    for i in CurrentHate:
        await client.say(i)
   
    await client.say('Would you like to add Hate?')
    await client.wait_for_message( content='Yes')     
    await client.say('what would you like to add?')
    await client.say("you're suggestion has been made.")                            
                    
    
    
@client.command(name='H8Ball',
                description = "I will tell you what you deserve to hear. you may type a question after the activation command.",
                aliases = ["h8ball", "H8ball", "h8Ball"],
                pass_context = True)

async def hateBall(context):
      global CurrentHate

      await client.say(random.choice(CurrentHate)+ ' ' + context.message.author.mention)







@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def ready():
    await client.change_presence(game=Game(name='with mortals'))
    print ('Logged in as ' + client.user.name)
    

client.run(Token)

input()