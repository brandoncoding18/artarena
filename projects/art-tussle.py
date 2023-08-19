import discord
from discord.ext import commands
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mydb import *

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)





members = []
pending_attacks = []
pending_images = []
pending_charid = []
pending_quality = []
pending_auth = [] 
permitted_channel_id = 1136358266868346950


class Attack: 

    def __init__(self, attacker, recipient, url, charid, quality, auth):
        self.attacker = attacker
        self.recipient = recipient
        self.url = url
        self.charid = charid
        self.quality = quality 
        self.auth = auth

    def getAttacker(self): 
        return self.attacker
    
    def getRecipient(self): 
        return self.recipient
    
    def getUrl(self):
        return self.url

    def getCharID(self):
        return self.charid


    def getQuality(self):
        return self.quality

    def getAuth(self): 
        return self.auth
    #

    def setRecipient(self, recipient):
        self.recipient = recipient
    
    def setUrl(self, url):
        self.url = url

    def setCharID(self, charid):
        self.charid = charid

    def setQuality(self, quality):
        self.quality = quality

    def setAuth(self, auth): 
        self.auth = auth 

    def __str__ (self):
        return "Attacker:" + str(self.attacker) + "\nRecipient:" + str(self.recipient) +  "\nUrl:" + str(self.url) +  "\nCharID:"+ str(self.charid) +  "\nQuality:" + str(self.quality) +  "\nAuth:" + str(self.auth) +  "\n"
    

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
# Method calls on startup
# 
@bot.event
async def on_ready():
    dropAll()
    insert = []
    i = 0 
    for guild in bot.guilds:
        for member in guild.members:
            i += 1
            members.append(str(member.id))
            insert.append({ "_id" : member.id})

    insertMany("Users", insert)
    

async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

@bot.event
async def on_member_join(member):
    members.append(str(member.id))
    #Database insert (snowflake, username)
    


@bot.event
async def on_member_remove(member):
    members.remove(str(member.id))
    #Database remove (snowflake, username)


async def sendDm(id, content):
    user = await bot.fetch_user(id)
    await user.send(str(content))


@bot.event  
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(str(reaction))


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    channel = bot.get_channel(int(permitted_channel_id)) 
    print(message.channel.type)

    if(not str(message.author) == "Art Arena#4949"):
        if(str(message.channel.type) == "private"):
            local_url = ""
            recipient =  None
            img = (message.attachments)
            index = 0
            for i in range(0, len(pending_attacks)):
                    if(pending_attacks[i].getAttacker().id == message.author.id):
                        recipient = pending_attacks[i].getRecipient()
                        index = i
                        print("hiiiii")

            print(pending_attacks[index])
            if(message.author in pending_images and len(img) == 1):
                
                
                img = str(img)
                await message.channel.send(str(message.attachments))
                url = img[img.index("url"): len(img)].replace("url=", "").replace(">]", "").replace("\'", "")
                await message.channel.send(url)
                print(url)
                ftype = url.split('/')[-1]
                myfile = requests.get(url)
                local_url = f'/tmp/file.{ftype}'
                open(local_url, 'wb').write(myfile.content)
                pending_images.remove(pending_attacks[index].getAttacker())
                pending_attacks[index].setUrl(local_url)
                await message.channel.send(str(pending_attacks[index]))
                await message.channel.send("Please submit character id")

            elif(message.author in pending_charid):
                pending_attacks[index].setCharID(message.content)
                await message.channel.send(str(pending_attacks[index]))

                pending_charid.remove(pending_attacks[index].getAttacker())
                await message.channel.send("Please submit quality:\n1: Rough sketch\n2: Finished Lineart\n3:Rough sketch with color\n4: Clean Color no shading\n5: Clean Color Minimal Shading\n6:Clean Color Complex Shading")




            elif(message.author in pending_quality):
                if(message.content in ["1", "2", "3", "4", "5", "6"]):
                    pending_attacks[index].setQuality(message.content)
                    await message.channel.send(str(pending_attacks[index]))
                    pending_quality.remove(pending_attacks[index].getAttacker())
                    await message.channel.send("Please confirm your attack:(Y/N)")

            elif(message.author in pending_auth):
                if(message.content.lower() == "y"):
                    await message.channel.send("Submitting Attack")
                    pending_auth.remove(pending_attacks[index].getAttacker())
                    pending_attacks[index].setAuth("approved")

                    channel = await bot.fetch_channel(permitted_channel_id)
                    #await channel.send(file=discord.File(local_url))
                    thread = await channel.create_thread(name="Attack:" , type=discord.ChannelType.private_thread)
                    id = str(hash(recipient))
                    attacker =  str(message.author.id)
                    recipient = str(pending_attacks[index].getRecipient())
                    character = str(pending_attacks[index].getCharID()) 
                    quality = str(pending_attacks[index].getQuality())
                    score = str(pending_attacks[index].getQuality())
                    image = str(pending_attacks[index].getUrl())
                    

                    await thread.send("Attack thread with id: " + str(hash(recipient)) + 
                                    "\nAttacker: <@" + attacker + ">" +  
                                    "\nRecipient: <@" + recipient + ">" +
                                    "\nCharacter: " + character +
                                    "\nQuality: " + quality +
                                    "\nCalculated Score: " + score)
                    await thread.send(file=discord.File(str(pending_attacks[index].getUrl())))
                    await thread.send("Attack log will be updated shortly")
                    mylist = [{ "_id" : 1, "attacker" : attacker, "recipient" : recipient, "character" : character, "quality" : quality, "score" : score, "url" : image}]
                    insertMany("Attacks", mylist)

                    #insert database attack(id, attacker, recipient, image, char_id)




                    
                elif(message.content.lower() == "n"):
                    await message.channel.send("Please resubmit the image for your attack")
                    pending_images.append(pending_attacks[index].getAttacker())
                    pending_charid.append(pending_attacks[index].getAttacker())
                    pending_quality.append(pending_attacks[index].getAttacker())
                else: 
                    await message.channel.send("Please respond with either Y or N")

            

                #this is where database insert happens 

            #await message.channel.send(str(message.attachments))
       










        if(message.channel.id == permitted_channel_id):
            msg = str(message.content)
            msg = msg.split(" ")
            print(msg)

            if(str(msg[0]) + " " + str(msg[1])  == "kill yourself"):
                await message.channel.send("Disconnecting")
                await bot.close()
            if(msg[0] == "/attack"):
                recipient_id = msg[1].replace("<", '').replace(">", '').replace("@", '')

                #IF THE ID OF THE ATTACKER IS THE SAME AS THE RECIPIENT, REJECT 
                #if(str(recipient_id) == str(message.author.id)): 
                    #await message.channel.send("Cannot attack user with same id")
                    
                #IF THE ID OF THE ATTACKER IS IN THE LIST OF MEMBERS
                if(recipient_id in members):
                    await message.channel.send("Attacking " + msg[1])
                    await message.channel.send("Please check your direct messages for instructions on your submission: " + "<@" + str(message.author.id) + ">")
                    recipient = await bot.fetch_user(str(recipient_id))
                    recipient = recipient.id
                    attacker = message.author
                    print("hiiiiiiiiii")
                    pending_attacks.append(Attack(attacker, recipient, "", "", "", ""))
                    pending_images.append(attacker)
                    pending_charid.append(attacker)
                    pending_quality.append(attacker)
                    pending_auth.append(attacker)
                    await sendDm(message.author.id,  "Please submit the image you would like to submit as an attack")








                    #hash = 12345
                    #thread = await channel.create_thread(name="Attack " + str(hash), type=discord.ChannelType.private_thread)
                    #await thread.send("Attack thread with id: " + str(hash) + 
                                    # "\nAttacker: <@" + str(message.author.id) + ">" +  
                                    # "\nRecipient: " + msg[1] +
                                    #  "\nCharacter: [id: char_name]" +
                                    #   "\nQuality: [quality]" + 
                                    #   "\nCalculated Score: [score]")
                    # await thread.send(file=discord.File('sample_attack.jpg'))
                    #await thread.send("Attack log will be updated shortly")
                    #this is where database insert happens 


                else: 
                    await message.channel.send("User not found")
                    
                
                            

                        
                #await message.channel.send("no arguments given \n\n Commands: \n\n /attack [user] [] ")
            
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
bot.run("MTEzNjkxMDEzODIxNzg3NzUwNg.GZJKol.eDuO3ftLNHYy7SIPpsA2AMbrRGG4-w9XX9bqRA")