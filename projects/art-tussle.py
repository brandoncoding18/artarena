import discord
from discord.ext import commands

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)

members = {}
attack = 0
permitted_channel_id = 1136358266868346950

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    #channel = bot.get_channel(1136358266868346950)
    #await channel.send("hiiiii")
    for guild in bot.guilds:
        for member in guild.members:
            #print(member)
            if(member.nick):
                members[member.nick] = str(member.id)
            members[member.display_name] = str(member.id)
            members[member.name] = str(member.id)
            members["<@" + str(member.id) + ">"] = str(member.id)

    print(members)
    
# EVENT LISTENER FOR WHEN THE BOT NOTICES A CHANGE IN NICKNAME.

@bot.event
async def on_member_update(before, after): 
    member = before 
    if(member.nick):
        del members[member.nick]
            
    del members[member.name]
    del members["<@" + str(member.id) + ">"]

    member = after
    members[member.display_name] = str(member.id)
    members[member.name] = str(member.id)
    members["<@" + str(member.id) + ">"] = str(member.id)
    print(members)


@bot.event
async def on_user_update(before, after): 
    member = before 
        
    del members[member.display_name]
    del members[member.name]
    del members["<@" + str(member.id) + ">"]

    member = after
    members[member.display_name] = str(member.id)
    members[member.name] = str(member.id)
    members["<@" + str(member.id) + ">"] = str(member.id)
    print(members)


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    if(message.channel.id == 1136358266868346950 and not str(message.author) == "Arttussle#3770"):
        msg = str(message.content)
        msg = msg.split(" ")
        print(msg)
        if(msg[0] == "/attack"):
            try:
                if(msg[1] in members):
                    await message.channel.send("Attacking <@" + members[msg[1]] + ">")
                else: 
                    await message.channel.send("User not found")

                
            except: 
                await message.channel.send("no arguments given \n\n Commands: \n\n /attack [user] [] ")
        
        if(message.content == "/fight-history"):
           await message.channel.send("No fights are recorded for this user")

        




    
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTEzNjM1NzU1NjIyNzQwODA3Mg.GmrYwg.Jx74TZKNAqSnxVnZPIBPLDacBZRVrxGRDWYRps")