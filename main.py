import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import os
import asyncio
import random
import requests
import json

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
async def on_message(message):
    global naughtypinger
    global naughtypingerid
    global naughtypingmsg
    if bot.user.mentioned_in(message):
        naughtypingerid = message.author.id
        naughtypinger = message.author.name
        naughtypingmsg = message.content
    await bot.process_commands(message)

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

@bot.command()
async def dailyos(ctx, dailyosnum:str):
    link = "https://raw.githubusercontent.com/nikolan123/daily-os/main/" + dailyosnum + ".md"
    print(link)
    f = requests.get(link)           
    await ctx.send(f.text)

@bot.command()
async def hack(ctx):
    await ctx.send("`hacked successfully`")

@bot.command()
async def whoping(ctx):
    await ctx.send(f"```who pinged \n\nuser: {naughtypinger} \nid: {naughtypingerid} \ncontent: '{naughtypingmsg}'```")


@bot.command()
async def cleardm(ctx, user: discord.User, purgenum:int):
    #await ctx.channel.purge(limit=5)
    count = 1
    async for message in user.history():
        if count<purgenum:
            if message.author == bot.user:
                await message.delete()
                count=count+1

@bot.command()
async def dogfact(ctx):
    dogfacturl = "https://dogapi.dog/api/v2/facts"
    querystring = {"limit":"1"}
    payload = ""
    response = requests.request("GET", dogfacturl, data=payload, params=querystring)
    response_json = json.loads(response.content)
    fact = response_json['data'][0]['attributes']['body']
    await ctx.send(f"```dog fact \n\n{fact}```")



TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
