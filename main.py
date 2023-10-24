import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Create a dictionary to store member data with criteria1, criteria2, criteria3, and committee
f = open("member_data.json", "r")
member_data = eval(f.read())

def has_allowed_role(*allowed_roles):
    async def predicate(ctx):
        author_roles = [role.name for role in ctx.author.roles]
        allowed = any(role in allowed_roles for role in author_roles)
        if not allowed:
            await ctx.send("You don't have permission to use this command.")
        return allowed
    return commands.check(predicate)

def save_file():
    with open("member_data.json", "w") as f:
        f.write(str(member_data))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def say(ctx, *text):
    my_str = ' '.join(text)
    await ctx.send(my_str)

@bot.command()

async def rate(ctx, member: str, criteria1: int = 0, criteria2: int = 0, criteria3: int = 0):
    member_data[str(member)] = {
        "criteria1": criteria1,
        "criteria2": criteria2,
        "criteria3": criteria3,
        "committee": member_data[str(member)]["committee"],
        "country": member_data[str(member)]["country"]

    }
    await ctx.send(f"{member}'s data has been set!")
    save_file()
@bot.command()
async def view(ctx, member: str):
    data = member_data.get(str(member))
    if data:
        criteria1 = data.get("criteria1")
        criteria2 = data.get("criteria2")
        criteria3 = data.get("criteria3")
        committee = data.get("committee")[0]
        country = data.get("country")[0]
        await ctx.send(f"{country,member}'s Data:\nCriteria 1: {criteria1}\nCriteria 2: {criteria2}\nCriteria 3: {criteria3}\nCommittee: {committee}\nOverall ranking: {(criteria1+criteria2+criteria3)/3}")
    else:
        await ctx.send("Member data not found.")
@bot.command()
@has_allowed_role('IT TEAM')
async def leaderboard(ctx, committee: str):
    # Check if the specified committee exists in the data
    if committee not in set(data.get('committee', '') for data in member_data.values()):
        await ctx.send(f"No members found in the committee '{committee}'.")
        return

    # Calculate the total points for each member in the specified committee
    committee_members = [
        (member, data) for member, data in member_data.items() if committee in data.get('committee', [])
    ]

    # Sort committee members based on the total points
    sorted_members = sorted(committee_members, key=lambda x: sum(x[1].values()), reverse=True)
    top_10 = sorted_members[:10]

    leaderboard_message = f"**Top 10 Delegates in {committee} (Total Points):**\n"
    for i, (member, data) in enumerate(top_10, start=1):
        total_points = sum(data.values())
        leaderboard_message += f"{i}. {member} - {total_points} points\n"

    await ctx.send(leaderboard_message)

@bot.command()
@has_allowed_role("IT TEAM")
async def send(ctx):
    with open('my_image.jpg', 'rb') as f:
        pict = discord.File(f)
        await ctx.send(file=pict)

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
bot.run('MTEzOTU3NjIwODE4NzcyODAyMw.G4cvq-.p7srAADXziLUjL00LPVtdjEwzM0-8w6tsBGM6c')
