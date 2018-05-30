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
    print(f"""\n=======================
I'm ready!
Logged in as:
{bot.user.name}
ID:{str(bot.user.id)}
Current prefix: {prefix}
Python Version: {sys.version_info[0]}
Discord Version: {discord.version_info}
========================\n""")
    """Quite self-explanatory"""
    async def change_activities():
        options = ('Minesweeper', 'Pong', 'Tic-tac toe', 'with the Discord API')
        timeout = 60
        watch = discord.Activity(type=discord.ActivityType.watching, name=f"for {prefix}help")
        stream = discord.Streaming(url="<your twitch link>", name="bits of information")
        listen = discord.Activity(type=discord.ActivityType.listening, name="to beeps and bops")
        while True:
            game = discord.Game(name=random.choice(options))
            possb = random.choice([watch, stream, game, listen])
            await bot.change_presence(activity=possb)
            await asyncio.sleep(timeout)

    # To fire up the worker in the background:
    bot.loop.create_task(change_activities())

    channel = utils.get(guild.channels, name="<the channel name you wanna send a Boot-up success message>")
    await channel.send(":white_check_mark: {bot.user.name} successfuly booted-up!")


bot.run(TOKEN)
