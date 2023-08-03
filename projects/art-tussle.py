import discord
from discord.ext import commands

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)

members = []
permitted_channel_id = 1136358266868346950

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
# Method calls on startup
# 
@bot.event
async def on_ready():
    
    for guild in bot.guilds:
        for member in guild.members:
            members.append(str(member.id))
    print(members)


@bot.event
async def on_member_join(member):
    members.append(str(member.id))
    


@bot.event
async def on_member_remove(member):
    members.append(str(member.id))



@bot.event  
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(str(reaction))


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    channel = bot.get_channel(int(permitted_channel_id)) 
    if(message.channel.id == 1136358266868346950 and not str(message.author) == "Arttussle#3770"):
        msg = str(message.content)
        msg = msg.split(" ")
        print(msg)
        if(msg[0] == "/attack"):
             
            if(msg[1].replace("<", '').replace(">", '').replace("@", '') in members):
                await message.channel.send("Attacking " + msg[1])
                thread = await channel.create_thread(name="thread", type=discord.ChannelType.public_thread)
                await thread.send("omg hiiiiiiii <@" + str(message.author.id) + "> " + msg[1])
            else: 
                await message.channel.send("User not found")
            
                
                    

                
            #except: 
                await message.channel.send("no arguments given \n\n Commands: \n\n /attack [user] [] ")
        
        if(message.content == "/fight-history"):
           await message.channel.send("No fights are recorded for this user")

        




    
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTEzNjM1NzU1NjIyNzQwODA3Mg.GmrYwg.Jx74TZKNAqSnxVnZPIBPLDacBZRVrxGRDWYRps")