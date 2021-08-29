import discord

class DiscordHooks:

    def __init__(self):
        self.client = discord.Client()

    def connect(self):
        print('Ready to start connection')

