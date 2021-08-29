import discord

class DiscordHooks:

    def __init__(self):
        self.client = discord.Client()

    def connect(self, token):
        print('Ready to start connection')
        self.client.run(token)

    def getHandle(self):
        return self.client
