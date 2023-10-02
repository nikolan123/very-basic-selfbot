import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import os
import asyncio
import random

load_dotenv()

bot = commands.Bot(command_prefix='h!', self_bot=True)

@bot.event
async def on_ready():
    print('--------------------')
    print('logged in as')
    print('user:' + bot.user.name)
    print('--------------------')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def whois(ctx, user:discord.User):
    await ctx.send(f'```user info\n\nusername: {user.name}#{user.discriminator}\nid: {user.id}```')

@bot.command()
async def avatar(ctx, user:discord.User):
    url = user.avatar.url
    await ctx.send(url)

@bot.command()
async def randnum(ctx,num1:int,num2:int):
    await ctx.send(f"```random number\n\nyour number is: {random.randint(num1,num2)}```")

snipe_message_content = None
snipe_message_author = None

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@bot.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@bot.command()
async def snipe(ctx):
    if snipe_message_content==None:
        await ctx.send(f"```snipe \n\ntheres nothing to snipe```")
    else:
        await ctx.send(f"```snipe \n\nuser with id {snipe_message_author} sent '{snipe_message_content}' with msg id {snipe_message_id}```<@{snipe_message_author}>")
        return

@bot.command()
async def gh(ctx, repo:str):
    await ctx.send(f"```github repo```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||https://github.com/{repo}")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
