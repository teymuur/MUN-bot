# version 0.8 pre-alpha
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)
f = open("ratings.json", "r")

ratings= eval(f.read())
f.close()
def has_allowed_role(*allowed_roles):
    async def predicate(ctx):
        author_roles = [role.name for role in ctx.author.roles]
        allowed = any(role in allowed_roles for role in author_roles)
        if not allowed:
            await ctx.send("You don't have permission to use this command.")
        return allowed
    return commands.check(predicate)
def save_file():
    f = open("ratings.json", "w")
    f.write(str(ratings))
    f.close()
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def say(ctx,*text):
    my_str = ' '.join(text)
    await ctx.send(my_str)
@bot.command()
async def talk(ctx,*aa):
    a = ''.join(aa)
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
@has_allowed_role('IT TEAM') 
async def set(ctx,member:discord.Member,rating=0):
    ratings[str(member)] = rating
    await ctx.send(member.display_name+"'s rating has been set!")
    save_file()
@bot.command()
@has_allowed_role('IT TEAM')  
async def rate(ctx, member: discord.Member):
    if ratings.get(str(member)):
        await ctx.send(str(ratings.get(str(member)))+"/10")
    else:
        await ctx.send("User hasnt been rated before also uwu~")

@bot.command()
@has_allowed_role() 
async def send(ctx):

    with open('my_image.jpg', 'rb') as f:
        pict = discord.File(f)
        await ctx.send(file=pict)
# Replace 'YOUR_TOKEN_HERE' with your actual bot token
bot.run('TOKEN')
