import discord
from discord.ext import commands
import requests
import json
import random
import music

cogs = [music]

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')

for i in range(len(cogs)):
    cogs[i].setup(client)

hello_word = ["-hi", "-hello", "-hey", "-yo"]
reply_word = [
    'hi there!', 'hello!', '*yoooo~*', '__What can I do for you!__',
    '***Hiiiii***'
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/quotes")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def get_joke():
    response = requests.get(
        'https://geek-jokes.sameerkumar.website/api?format=json')
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return (joke)


@client.event
async def on_ready():
    await client.change_presence(activity= discord.Game('YU digital media')) 
    print('Logged on as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.content.startswith('!hug'):
      await message.channel.send(f"hugs {message.author.mention}")

    # if message.content.startswith('!123'):
    #   await message.channel.send(f"hugs {message.author.mention} + {user_mention}")      
     
    if message.author == client.user:
        return

    if message.content == "-help":
        myEmbed = discord.Embed(
            title="The Guide!",
            description="Here you can find all the commands about me",
            color=0xFFA500)
        # myEmbed.set_author(name = 'Yizhi Zhou',icon_url= 'https://cdn.discordapp.com/attachments/947645379602710541/948022266707451904/11.jpg')
        myEmbed.add_field(name="-hi/-hello/-yo/-hey ...",
                          value="I will say hello to you!",
                          inline=False)
        myEmbed.add_field(
            name="-quote",
            value="I will give you a quote! (Avada Kedavra! <nvm>) ",
            inline=False)
        myEmbed.add_field(
            name="-joke",
            value=
            "I will tell you a funny joke or lame joke maybe... lol (it depends) ",
            inline=False)
        myEmbed.add_field(
            name="!ping",
            value=
            "Type it to see the current ping",
            inline=False)
        myEmbed.add_field(
            name="!repeat [...]",
            value=
            "I will repeat what you said!\n Example: !repeat I am smart",
            inline=False)  
        myEmbed.add_field(
            name="!rn / !ln",
            value=
            "To get a random/lucky number (0-100)",
            inline=False)
        myEmbed.add_field(
            name="!rps [rock/paper/scissors]",
            value=
            "Play rock-paper-scissors with me!\n Example: !rps rock",
            inline=False)
        myEmbed.add_field(
            name="-music",
            value=
            "This involves all the commands for music part",
            inline=False)
        myEmbed.add_field(
            name="-info",
            value=
            "View the current bot's information and my contact information",
            inline=False)
        myEmbed.set_footer(
            text="Yizhi Zhou             modified on 2022/2/27",
            icon_url=
            'https://cdn.discordapp.com/attachments/947645379602710541/948011660419944478/88D4B6FAD383D4B4D02B1733D5873FFC.png'
        )
        myEmbed.set_thumbnail(
            url=
            'https://cdn.discordapp.com/attachments/947645379602710541/948022266707451904/11.jpg'
        )
        await message.channel.send(embed=myEmbed)

    if message.content == "-info":
        myEmbed = discord.Embed(title="Information",
                                description="This bot is made by Yizhi Zhou",
                                color=0x00ff00)
        myEmbed.add_field(name="Current Version", value="v1.0.5", inline=False)
        myEmbed.add_field(name="Date Released",
                          value="February 23, 2022",
                          inline=False)
        myEmbed.add_field(name="Last update on",
                          value="March 2, 2022",
                          inline=False)
        myEmbed.add_field(name="My Discord:",
                          value=" imnsss#1317 ",
                          inline=True)
        myEmbed.add_field(name="My Email:",
                          value=" zhouyizhi1030@gmail.com ",
                          inline=True)
        await message.channel.send(embed=myEmbed)

    if message.content == "-music":
        myEmbed = discord.Embed(title="Music!",
                                description="Play youtube audio for you. Currently, only YouTube Link is supported",
                                color=0x8A2BE2)
        myEmbed.add_field(name="!join", value="I will join your current voice channel (but you need to join a voice channel first :P) ", inline=False)
        myEmbed.add_field(name="!leave",
                          value="I will leave the voice channel!",
                          inline=False) 
        myEmbed.add_field(name="!play [youtube link]",
                          value="I will play the audio of the given YouTube link\nExample: !play https://www.youtube.com/watch?v=6Q0Pd53mojY",
                          inline=False) 
        myEmbed.add_field(name="!pause",
                          value="I will pause the current song.",
                          inline=False) 
        myEmbed.add_field(name="!resume",
                          value="I will resume the current song.",
                          inline=False) 
        await message.channel.send(embed=myEmbed)

    if any(word in message.content for word in hello_word):
        await message.channel.send(random.choice(reply_word))

    if message.content.startswith('-quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('-joke'):
        joke = get_joke()
        await message.channel.send(joke)

    

    await client.process_commands(message)

@client.command()
async def ping(ctx):
  await ctx.send(f"current ping: {round(client.latency * 1000)}ms")

@client.command(aliases=['repeat'])
async def _repeat(ctx, *, answer):
  await ctx.send(f'{answer}')

@client.command(aliases = ['rn'])
async def ln(ctx):
  responses = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
  await ctx.send(f'Lucky number: {random.choice(responses)}')

# @client.command()
# async def rps(ctx, *, test):
#   responses = [':fist:', ':v:', ':hand_splayed:']
#   await ctx.send(f'Your choice: {test} \nMy choice {random.choice(responses)}')    

@client.command(help="Play with .rps [your choice]")
async def rps(ctx, user_choice):
    rps = ['rock', 'paper', 'scissors']

    bot_choice = random.choice(rps)
    user_choice = user_choice.lower()
  
    if user_choice == 'rock':
        if bot_choice == 'rock':
            await ctx.send(f'Oops! we tied. \n\nYour choice: {user_choice}\nMy choice: {bot_choice}')
        elif bot_choice == 'paper':
            await ctx.send(f'Haha I won!\n\nYour choice: {user_choice}\nMy choice: {bot_choice}')
        elif bot_choice == 'scissors':
            await ctx.send(f"Aw, you beat me.\n\nYour choice: {user_choice}\nMy choice: {bot_choice}")

    elif user_choice == 'paper':
        if bot_choice == 'rock':
            await ctx.send(f"Can't believe I lost!\n\nYour choice: {user_choice}\nMy choice: {bot_choice}")
        elif bot_choice == 'paper':
            await ctx.send(f'Oh! We just tied.\n\nYour choice: {user_choice}\nMy choice: {bot_choice}')
        elif bot_choice == 'scissors':
            await ctx.send(f"Aha! I won!!\n\nYour choice: {user_choice}\nMy choice: {bot_choice}")

    elif user_choice == 'scissors':
        if bot_choice == 'rock':
            await ctx.send(f'Lol, I won!!\n\nYour choice: {user_choice}\nMy choice: {bot_choice}')
        elif bot_choice == 'paper':
            await ctx.send(f'oh no!!!You won!\n\nYour choice: {user_choice}\nMy choice: {bot_choice}')
        elif bot_choice == 'scissors':
            await ctx.send(f"Okay, we tied :P\n\nYour choice: {user_choice}\nMy choice: {bot_choice}")  


client.run('OTQ3NTc3NTQ1NDUxMjQ5NjY0.YhvSWw.1Wr0umcV8qjY_HdAEnhpnh7eg1I')
