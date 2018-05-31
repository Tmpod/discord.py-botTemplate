__version__ = '<your bot version>'
"""Imports"""
import discord
from discord.ext import commands
#import logging #This is not necessary
#import traceback #This is not necessary

"""Setting up loggin"""
#logging.basicConfig(level='INFO')
#logger = logging.getLogger('thisfile.py')

"""Getting your bot token from a external file so that you can share your code easily without having to always black it out"""
with open('./yourfilecontainingONLYyourbottoken.txt') as fp:
    TOKEN = fp.read().strip()

prefix = "<your bot prefix>" #It's really useful to define the prefix in a seperate variable instead of just putting it directily in the 'command_prefix' paramter

bot = commands.Bot(description="<your bot description>", command_prefix=prefix)

"""This piece of code loads all the extensions delcared on the 'extensions' varaiable"""
#extensions = ['module1', 'module2'] #You can have as many extensions as you want

#for extension in extensions:
#    try:
#        bot.load_extension(extension)
#    except Exception:
#        print(globals())
#        logger.error(f'Failed to load {extension} with error:\n{traceback.format_exc()}')

"""Removing the default help command so that you can make a better and fancier one later. Not mandatory."""
#bot.remove_command('help')

"""Boot-up code"""
@bot.event
async def on_ready():
    creator = (await bot.application_info()).owner # This may seem a bit more complicate but all it does is get the bot owner
    print(f"""\n===========================
I'm ready!
Welcome to {bot.user.name}!
ID: {str(bot.user.id)}
Creator: {creator}
Current prefix: {prefix}
Python Version: {sys.version_info[0]}
Discord Version: {discord.version_info[0]}
CyborgToast Version: {__version__}
===========================\n""")
    """Quite self-explanatory"""
    async def change_activities():
        options = ('Minesweeper', 'Pong', 'Tic-tac toe', 'with the Discord API') # All the options for the "Playing <smth>" status
        timeout = 60  # The time between each change of status
        watch = discord.Activity(type=discord.ActivityType.watching, name=f"for {prefix}help") # "Watching <smth>" status
        stream = discord.Streaming(url="<your twitch link>", name="bits of information") # "Streaming <smth>" status
        listen = discord.Activity(type=discord.ActivityType.listening, name="to beeps and bops") # "Listening <smth>" status
        while True: # Infinite loop
            game = discord.Game(name=random.choice(options)) # Pick a choice from 'options'. Watch out for how you import 'random', as that might affect how this line needs to be written. For more help refer to the Python Docs.
            possb = random.choice([watch, stream, game, listen]) # Pick a choice from all the possibilities: "Playing", "Watching", "Streaming", "Listening" or "Playing"
            await bot.change_presence(activity=possb) # Now change the status to the chosen pick
            await asyncio.sleep(timeout) # And wait for 'timeout' seconds

    bot.loop.create_task(change_activities())  # To fire up the worker in the background:

    channel = bot.get_channel('<channel id in a int>') # Gets a discord.TextChannel from the id you insert. YOU MUST INSERT A INT, I've put a string because of syntax highlighting
    await channel.send(f":white_check_mark: {bot.user.name} successfuly booted-up!") # And sends a message there



# Your commands here #



bot.run(TOKEN) # Actually running the bot running
