"""Basic imports"""
import discord
from discord.ext import commands


with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']


class youcogname:
    def __init__(self, bot):
        self.bot = bot

    # Your commands here. Remmeber to user '@commands.command' instead of '@bot.commands'. If you wanna use something that uses 'bot' don't forget to put 'self.' before. Eg: 'bot.latency' would be 'self.bot.latency' #


"""Defining this extension"""
def setup(bot):
    bot.add_cog(yourcogname(bot))