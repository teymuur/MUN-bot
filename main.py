import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='_', intents=intents)
f = open("ratings.json", "r")

ratings= eval(f.read())
f.close()
def save_file():
    f = open("ratings.json", "w")
    f.write(str(ratings))
    f.close()
@bot.event
async def on_ready_():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def say_(ctx,*text):
    my_str = ' '.join(text)
    await ctx.send(my_str)
@bot.command()
async def talk_(ctx,*aa):
    a = aa.join(' ')
    a = a.lower()
    if "purpose" in a :
        response = 'This command has been made for Omar to sense female attention, No need to thank'
    elif "credit" in a:
        response = "Created by Teymur in behalf of the Sabis Sun Mun It Team. Original Idea: kakoyta Omar"
    elif 'love' in a:
        response = 'Love you too honey~'
    elif "hug" in a:
        response = "*Hugs you tightly* Don't worry, everything will be okay!"
    elif "date" in a:
        response = "I'd love to go on a virtual date with you! Where should we go?"
    elif "music" in a or "artist" in a:
        response = "Let's listen to some music together! What's your favorite genre? I am a Slipknot fan"
    elif "dream" in a:
        response = "Tell me about your dreams! I'm here to listen and support you."
    elif "movie" in a:
        response = "I'm in the mood for a movie night. What genre do you prefer?"
    elif "exercise" in a:
        response = "Staying active is important! How about we do a quick workout together?"
    elif " l " in a:
        response = "L yourself bitch"
    elif "angry" in a and "you" in a:
        response = "Who is angry I am not angry I AM SO CALM LOOK AT ME"
    elif "bye" in a:
        response = "Goodbye! Take care, and remember I'm always here for you!"
    elif "pic" in a or "picture" in "a":
        with open('my_image.jpg', 'rb') as f:
            pict = discord.File(f)
            await ctx.send(file=pict)
    else:
        response = "I'm not sure how to respond to that. Can you be more specific?"
    await ctx.send(response)
@bot.command()
async def set_(ctx,member:discord.Member,rating=0):
    ratings[str(member)] = rating
    await ctx.send(member.display_name+"'s rating has been set!")
    save_file()
@bot.command()
async def rate_(ctx, member: discord.Member):
    if ratings.get(str(member)):
        await ctx.send(str(ratings.get(str(member)))+"/10")
    else:
        await ctx.send("User hasnt been rated before also uwu~")
        
bot.run('TOKEN_HERE')
