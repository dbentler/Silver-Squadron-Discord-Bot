"""
The main functionality of the bot should be in this main file. For any other functionality, either add it to "utilities.py" or create a new python file.
"""

import discord
from discord.ext import commands
from discord.ext import tasks

from utilities import *
from objects import *
from help_command import *

# Global Variables

EVENTS = {} # Dictionary for events. Stores events by message ID.
DIV = "\n------------"

# Grabbing secrets
secrets = get_secrets("secrets.txt")

# Bot set up
client = commands.Bot(command_prefix='$')

# EVENTS -------------------------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    print("Guardian: I'm ready to serve." + DIV)
    await alert.start()

@client.event
async def on_reaction_add(reaction, user):
    if (reaction.emoji == '✅') and (reaction.message.author.name != client.user):
        msg = "You've RSVP-ed to an event! You'll be reminded of the event an hour before it takes place."
        print(f"Sending dm to {user}")
        try:
            await user.send(msg)
            EVENTS[reaction.message.id].attendees.append(user)
            print(f"Successfully sent dm to {user}.")
        except:
            print(f"Couldn't send message to {user}. Continuing as if nothing happen.")
        return

# Commands -------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def helpme(ctx):
    for key in help_cmd:
        await ctx.send(f"> {key} {help_cmd[key]}")

@client.command()
async def hello(ctx):
    await ctx.send("Hello World")
    return

@client.command()
async def event(ctx, e_type=None, date=None, time=None, *description):
    syntax = "`$event <event type> <date> <time, EST/EDT> <description (optional)>`"

    # Commands to handle inproper syntax usage
    if ctx.message.author.name == client.user:
        return

    if (e_type == "help"):
        await ctx.send(syntax)
        return
    
    if (e_type or date or time) == None:
        await ctx.send("You need to specify the event's type, date, and time!")
        await ctx.send(syntax)
        return
    # Guardian is letting you know what it's up to.
    print(f"{ctx.message.author.name} wants to create a(n) {e_type} event. Creating...")

    try:
        # Event formatting stuff
        e_vent = Event(e_type, date, time, description)
        f_event = e_vent.__repr__()
        
        await ctx.send("**NEW EVENT** @here")
        msg = await ctx.send(f_event)
        
        # Adding emojis.
        emojis = ['✅', '❌', '❔']
        for emoji in emojis:
            await msg.add_reaction(emoji)
        # Finalizing Message
        await ctx.send("If you are attending, react with :white_check_mark:. If you're not, react with :x:. If you don't know, react with :grey_question:.")
        print(f"{ctx.message.author.name}'s event has been successfully created!" + DIV)
        # Adds event to EVENT dictionary.
        EVENTS[msg.id] = e_vent
        return

    except Exception as e:
        print("Something went wrong creating the event. Created new log file." + DIV)
        e = str(e)
        log(e)
        await ctx.send("Something went wrong! @N-6 - Information & Technology , please check the log files.")  
        return

@client.command()
async def caevents(ctx, code=None):
    # This will need to check for user permissions. Someone else can implement that at a later date.
    if ctx.message.author.name == client.user:
        return
    
    if code == "help" or code != "1234":
        await ctx.send("Clears all events.")
        return
    
    if code == "1234": # You can change the code here if you'd like.
        EVENTS.clear()
        await ctx.send("All events have been cleared.")
        return

@client.command()
async def events(ctx):
    for key in EVENTS:
        await ctx.send(f"> {EVENTS[key]._type}, {EVENTS[key].date}, {EVENTS[key].time}")
    return

@client.command()
async def op(ctx, *args):
    # Similar to $event, but takes in military format.
    syntax = f"`$op <time (HHMM) (EST/EDT)> <date (DDMMMYY)>`"
    
    description = "Silver Squadron's weekly ARMA 3 Operation."
    _type = "Operation"

    if ctx.message.author.name == client.user:
        return
    if ("help" in args):
        await ctx.send(f"Use the following syntax: {syntax}")
        return
    try:
        lst_conv = list(args)
        date = mil_to_civ(lst_conv[1])
        time = mt_to_ct(lst_conv[0])
        print(f"Creating operation event as requested by {ctx.message.author.name}.")
        # Event formatting stuff
        e_vent = Event(_type, date, time, description)
        f_event = e_vent.__repr__()
        await ctx.send("**NEW EVENT** @here")
        msg = await ctx.send(f_event)
        # Adding emojis.
        emojis = ['✅', '❌', '❔']
        for emoji in emojis:
            await msg.add_reaction(emoji)
        # Finalizing Message
        await ctx.send("If you are attending, react with :white_check_mark:. If you're not, react with :x:. If you don't know, react with :grey_question:.")
        print(f"{ctx.message.author.name}'s event has been successfully created!" + DIV)
        # Adds event to EVENT dictionary.
        EVENTS[msg.id] = e_vent
        return
    except Exception as e:
        e = str(e)
        log(e)
        await ctx.send("Something went wrong! @N-6 - Information & Technology , please check the log files.")  
        return

@client.command()
async def shoot(ctx, user=None):
    if user == None or user == "help":
        await ctx.send("Try to shoot someone! `$shoot <@user>`.")
        return
    from minigames import mini_shoot
    await ctx.send(mini_shoot(user))
    return
# Tasks -------------------------------------------------------------------------------------------------------------------------------------------
@tasks.loop(minutes=15.0)
async def alert():
    """
    TODO FIND A BETTER WAY TO DO THIS DO THIS STRING MANIPULATION
    """
    today = date()
    # Tomfoolery
    separator = today.find("_")
    _date = today[:separator]
    _date = _date.replace("-", "/")
    for key in EVENTS:
        if EVENTS[key].date == _date:
            # I actually hate myself.
            time_t = today[separator+1:]
            time_t = time_t.replace("-", ":")
            time_t = time_t[:5]
            time_t = convert_time(str(time_t))
            # Am I stupid?
            event_time = EVENTS[key].time.strip(" Eastern Standard Time (EST/EDT)")
            if(hour_out(time_t, event_time)):
                if len(EVENTS[key].attendees) != 0:
                    print("Sending out Event alerts...")
                    for user in EVENTS[key].attendees:
                        await user.send(f"{EVENTS[key]._type} is starting in 1 hour!")
                    EVENTS[key].attendees = []
                    print("Event alerts successfully sent out." + DIV)
            if(time_t == event_time):
                # TODO
                pass

if __name__ == "__main__":
    client.run(secrets[0])