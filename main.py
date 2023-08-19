#version 1.1-alpha
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot()
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

#commands
@bot.slash_command()
async def say(ctx,*text):
    my_str = ' '.join(text)
    await ctx.send(my_str)
@bot.slash_command()
async def talk(ctx,*aa):
    a = ''.join(aa)
    a = a.lower()
    if "purpose" in a :
        response = 'This command has been made for Omar to sense female attention, No need to thank'
    elif "credit" in a:
        response = "Created by Teymur in behalf of the Sabis Sun Mun It Team. Original Idea: kakoyta Omar"
    elif "life" in a and "what" in a:
        response = "I dont what life is I am just an MUN bot"
        await ctx.author.send("hello cutie pie~💕")
    elif "MUN" in a:
        response = "Sabis MUN is the best one"
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
@bot.slash_command()
@has_allowed_role('IT TEAM') 
async def set(ctx,member:discord.Member,rating=0):
    ratings[str(member)] = rating
    await ctx.send(member.display_name+"'s rating has been set!")
    save_file()
@bot.slash_command()
@has_allowed_role('IT TEAM')  
async def rate(ctx, member: discord.Member):
    if ratings.get(str(member)) != None:
        await ctx.send(str(ratings.get(str(member)))+"/10")
    else:
        await ctx.send("User hasnt been rated before also uwu~")

@bot.slash_command()
@has_allowed_role("IT TEAM") 
async def send(ctx):

    with open('my_image.jpg', 'rb') as f:
        pict = discord.File(f)
        await ctx.send(file=pict)



class MyView(discord.ui.View):

    
    @discord.ui.select(
        placeholder="What is your committee?",

        options = [
            discord.SelectOption(
                label="UNGA",
                description="Pick this if you are UNGA!"
            ),
            discord.SelectOption(
                label="UNSC",
                description="Pick this if you are UNSC!"
            ),
            discord.SelectOption(
                label="OHCHR",
                description="Pick this if you are OHCHR!"
            ),
            discord.SelectOption(
                label="ICJ",
                description="Pick this if you are ICJ!"
            ),
            discord.SelectOption(
                label="HSC",
                description="Pick this if you are HSC!"
            ),
            discord.SelectOption(
                label="UNRWA",
                description="Pick this if you are UNRWA!"
            )
        ]      
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        await interaction.user.send(f"Awesome! I like {select.values[0]} too!")
        await interaction.user.send("I can make you the best delegate just $5")



 # commitee selection not working properly yet some weird error   
@bot.slash_command()
@has_allowed_role("IT TEAM")
async def select_(ctx):
    view = MyView()
    await ctx.send(view=view)
        
    await view.wait()

        
    member = ctx.message.author
    print(view.answer1)
    await member.add_roles(view.answer1[0],view.answer2[0])

    await ctx.message.author.send("Hey~")


# Replace 'YOUR_TOKEN_HERE' with your actual bot token
bot.run('MTEzOTU3NjIwODE4NzcyODAyMw.GAjc81.BQczNXgCikpnCQzRLFcQV-FoOXGXfdwcucIhXc')
