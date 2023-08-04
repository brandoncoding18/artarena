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
            recipient_id = msg[1].replace("<", '').replace(">", '').replace("@", '')
            if(str(recipient_id) == str(message.author.id)): 
                await message.channel.send("Cannot attack user with same id")
                
            elif(recipient_id in members):
                await message.channel.send("Attacking " + msg[1])
                await message.channel.send("Please check your direct messages for instructions on your submission: " + "<@" + str(message.author.id) + ">")
                hash = 12345
                thread = await channel.create_thread(name="Attack " + str(hash), type=discord.ChannelType.private_thread)
                await thread.send("Attack thread with id: " + str(hash) + 
                                "\nAttacker: <@" + str(message.author.id) + ">" +  
                                "\nRecipient: " + msg[1] +
                                "\nCharacter: [id: char_name]" +
                                "\nQuality: [quality]" + 
                                "\nCalculated Score: [score]")
                await thread.send(file=discord.File('sample_attack.jpg'))
                await thread.send("Attack log will be updated shortly")


            else: 
                await message.channel.send("User not found")
            
          
                    

                
            #except: 
                await message.channel.send("no arguments given \n\n Commands: \n\n /attack [user] [] ")
        
        if(msg[0] == "/fight-history"):
            try: 
                target = msg[1].replace("<", '').replace(">", '').replace("@", '')
                if(target in members):
                    await message.channel.send("[Unimplemented Feature]")

                else: 
                    await message.channel.send("User not found")




            except:
                await message.channel.send("User not provided, please provide argument like so: /fight-history @[user]")

        if(msg[0] == "/leaderboard"):
            
            try: 
                if(msg[1]):
                    await message.channel.send("/leaderboard does not accept additional arguments")
                    

            except:
                await message.channel.send("[Unimplemented]")


        

        

        

        




    
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTEzNjM1NzU1NjIyNzQwODA3Mg.GmrYwg.Jx74TZKNAqSnxVnZPIBPLDacBZRVrxGRDWYRps")