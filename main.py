import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import os
import asyncio
import random
import requests
import json
import base64
import xpgembed
import subprocess

load_dotenv()

bot = commands.Bot(command_prefix='h!', self_bot=True)
mewords = ["nikolan", "767780952436244491"]
snitchchannel = 1161221086587932712

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
    avatarURL = f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png"
    await ctx.send(xpgembed.webEmbed(title="User Info", description=f"Username: {user.name}#{user.discriminator}\nID: {user.id}", thumbnail=avatarURL, color="#B8DAF4"))
    #await ctx.send(f'```user info\n\nusername: {user.name}#{user.discriminator}\nid: {user.id}```')

@bot.command()
async def avatar(ctx, *, member:discord.User):
    try:
        avatarURL = f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png"
        await ctx.send(xpgembed.webEmbed(title="Avatar", description=f"{member.name}'s avatar", thumbnail=avatarURL, bigimg=True, color="#B8DAF4"))
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def randnum(ctx,num1:int,num2:int):
    await ctx.send(xpgembed.webEmbed(title="Random Number Generator", description=f"Your number is: {random.randint(num1,num2)}", color="#B8DAF4"))
    #await ctx.send(f"```random number\n\nyour number is: {random.randint(num1,num2)}```")

#all of the sniping shit below
snipe_message_content = {}
snipe_message_author = {}

snipe_message_content = {}
snipe_message_author = {}
snipe_message_id = {}

@bot.event
async def on_message_delete(message):
    snipe_message_content[message.channel.id] = message.content
    snipe_message_author[message.channel.id] = message.author.id
    snipe_message_id[message.channel.id] = message.id
    snipe_channel = message.channel.id
@bot.command(name="snipe",description="Shows the last deleted message")
async def snipe(ctx):
    if snipe_message_content == None:
        await ctx.send(xpgembed.webEmbed(title="Snipe", description="Nothing to snipe", color="#B8DAF4"))
    else:
        # await ctx.send(f"```snipe \n\nuser with id {snipe_message_author} sent '{snipe_message_content}' with msg id {snipe_message_id}```<@{snipe_message_author}>")
        embed = discord.Embed(title="Snipe", color=0xB8DAF4)
        try:
            await ctx.send(xpgembed.webEmbed(title="Snipe", description=f"Author: {snipe_message_author[ctx.channel.id]}\nContent: {snipe_message_content[ctx.channel.id]}", color="#B8DAF4"))

            embed.add_field(
                name="Author",
                value=f"<@{snipe_message_author[ctx.channel.id]}>",
                inline=False,
            )
            embed.add_field(
                name="Message",
                value=f"{snipe_message_content[ctx.channel.id]}",
                inline=False,
            )
           
        except Exception as e:
            await ctx.send(xpgembed.webEmbed(title="Snipe", description="Nothing to snipe", color="#B8DAF4"))
        return

#end of sniping shit

@bot.event
async def on_message(message):
    global naughtypinger
    global naughtypingerid
    global naughtypingmsg
    if bot.user.mentioned_in(message):
        naughtypingerid = message.author.id
        naughtypinger = message.author.name
        naughtypingmsg = message.content
    snch = bot.get_channel(snitchchannel)
    snss = False
    for h in mewords:
        if h in message.content.lower() and snss == False and message.guild:
            try:
                thingy = message.guild.name
                thingy2 = message.guild.id
            except Exception as e:
                print(e)
                thingy = "DMs"
                thingy2 = "DMs"
            await snch.send(f"{message.author.mention} ({message.author.id}) used `{h}` in their message with content \n> {message.content}\n sent in '{thingy}' ({thingy2}) <#{message.channel.id}>")
            snss = True
    await bot.process_commands(message)

@bot.command()
async def gh(ctx, repo:str):
    await ctx.send(f"```github repo```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||https://github.com/{repo}")

@bot.command()
async def whoping(ctx):
    try:
        #await ctx.send(f"```who pinged \n\nuser: {naughtypinger} \nid: {naughtypingerid} \ncontent: '{naughtypingmsg}'```")
        await ctx.send(xpgembed.webEmbed(title="Who pinged", description=f"User: {naughtypinger}\nID: {naughtypingerid}\nContent: {naughtypingmsg}", color="#B8DAF4"))
    except Exception as e:
        await ctx.send(f"an error occured: {e}")


@bot.command()
async def cleardm(ctx, user: discord.User, purgenum:int):
    #await ctx.channel.purge(limit=5)
    #await ctx.send(xpgembed.webEmbed(title="Message Purger", description=f"Purging {purgenum} messages..."))
    #await asyncio.sleep(3)
    the = await ctx.send(xpgembed.webEmbed(description="Please wait while the Automated Computer script is performing non-verbal communication with the remote servers...", color="#B8DAF4"))
    count = 1
    async for message in user.history():
        if count<purgenum:
            if message.author == bot.user:
                await message.delete()
                count=count+1
    await the.edit(content=xpgembed.webEmbed(title="DM Purge Completed", description=f"Purged {purgenum} in DMs with {user.name}", color="#B8DAF4"))

@bot.command()
async def dogfact(ctx):
    the = await ctx.send(xpgembed.webEmbed(description="Please wait while the Automated Computer script is performing non-verbal communication with the remote servers...", color="#B8DAF4"))
    dogfacturl = "https://dogapi.dog/api/v2/facts"
    querystring = {"limit":"1"}
    payload = ""
    response = requests.request("GET", dogfacturl, data=payload, params=querystring)
    response_json = json.loads(response.content)
    fact = response_json['data'][0]['attributes']['body']
    #await ctx.send(f"```dog fact \n\n{fact}```")
    await the.edit(content=xpgembed.webEmbed(title="Dog Fact", description=fact, color="#B8DAF4"))

@bot.command()
async def hack(ctx):
    message = await ctx.send("```loading...```")
    for x in range(3):
        await asyncio.sleep(0.2)
        await message.edit(content=f"```downloading trojan /```")
        await asyncio.sleep(0.2)
        await message.edit(content=f"```downloading trojan |```")
        await asyncio.sleep(0.2)
        await message.edit(content=f"```downloading trojan \\```")
        await asyncio.sleep(0.2)
        await message.edit(content=f"```downloading trojan -```")
    await message.edit(content=f"```extracting \n3.5mb/s ■□□□□□□□□□ 10%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n5.7mb/s ■■■□□□□□□□ 30%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n5.6mb/s ■■■■□□□□□□ 40%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n5.7mb/s ■■■■■□□□□□ 50%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n0.2mb/s ■■■■■■□□□□ 60%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n1.3mb/s ■■■■■■■□□□ 70%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n10.7mb/s ■■■■■■■■□□ 80%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n4.5mb/s ■■■■■■■■■□ 90%```")
    await asyncio.sleep(0.5)
    await message.edit(content=f"```extracting \n2.9mb/s ■■■■■■■■■■ 100%```")
    await asyncio.sleep(0,5)
    await message.edit(content=f"```executed trojan.exe on victims pc```")


@bot.command()
async def whatareyou(ctx):
    await ctx.send(xpgembed.webEmbed(title="im nikolans selfbot :)", color="#B8DAF4"))

@bot.command()
async def ds(ctx, *, sdds):
    await ctx.message.delete()
    thett = await ctx.send(sdds)
    await thett.delete()

@bot.command()
async def doggo(ctx):
    the = await ctx.send(xpgembed.webEmbed(description="Please wait while the Automated Computer script is performing non-verbal communication with the remote servers...", color="#B8DAF4"))
    dogpicurl = "https://dog.ceo/api/breeds/image/random"
    payload = ""
    response = requests.request("GET", dogpicurl, data=payload)
    response_json = json.loads(response.content)
    doggo = response_json.get('message', "")
    await the.edit(content=xpgembed.webEmbed(title="Doggo", thumbnail=doggo, bigimg=True, color="#B8DAF4"))
    #await ctx.send(f"```doggo pic gen```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||{doggo}")

@bot.command()
async def ai(ctx, *, msgfr:str):
    the = await ctx.send(xpgembed.webEmbed(title="AI", description="Generating, please wait...", color="#B8DAF4"))
    result = subprocess.Popen('python gen.py ' + msgfr, stdout=subprocess.PIPE)
    result.wait()
    output, error = result.communicate()
    formatted_output = str(output).replace('\\n', '\n').replace('\\r', '\r').replace('b"', '').replace("b'", '').replace("@", "_").replace("##", "#").replace("\n'", "")
    await the.edit(content=f"> Generated using model GPT-3.5-Turbo\n{formatted_output}")


def check_website_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx status codes)
        return f"The website <{url}> is up. Status code: {response.status_code}"
        #return f"UP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"The website <{url}> is down. Error: {e}"
        #return "Down"
@bot.command(name="wping")
async def pingweb(ctx, web):
    the = await ctx.send(xpgembed.webEmbed(description="Please wait while the Automated Computer script is performing non-verbal communication with the remote servers...", color="#B8DAF4"))
    if "http://" in web or "https://" in web:
        pass
    else:
        web = "http://" + web
    result = check_website_status(web)
    await the.edit(content=xpgembed.webEmbed(description=result, color="#B8DAF4"))

@bot.command()
async def tokenstart(ctx, user: discord.User):
    b64_encoded = base64.b64encode(str(user.id).encode('utf-8')).decode('utf-8')
    b64_thingy = b64_encoded.replace('=', '')
    final = b64_thingy + '.'
    await ctx.send(xpgembed.webEmbed(title="Token", description=f"{user.name}'s token starts with:\n{final}", color="#B8DAF4"))

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
