import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = '.', help_command = None)

colorama.init()
os.system("title Login")
token = input("Token : ")
@client.event
async def on_ready():
 os.system("cls & title henry mass dm ")
 print(f'''
 
{Fore.YELLOW}   
              ╦ ╦╔═╗╔╗╔╦═╗╦ ╦  ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗
              ╠═╣║╣ ║║║╠╦╝╚╦╝  ║║║╠═╣╚═╗╚═╗   ║║║║║
              ╩ ╩╚═╝╝╚╝╩╚═ ╩   ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩

      Note: Make sure you have a phone number if you have a large\n number of friends. 50+ You should be aware           
{Fore.RED} [1] : Mass Dm
{Fore.RED} [2] : Credits                                           
''')
 H1 = input("Number : ")
 if H1 == '1':
  input2 = input("Message : ")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+]Messaged{Fore.RED} {input2} {Fore.YELLOW}To {user}")
 if H1 == '2':
   input("skidded by henry, we love u h1 <3 , https://discord.gg/zhM5fAEHAj for help")

client.run(token, bot = False)