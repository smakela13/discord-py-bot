import os
import sys
from .discord_hooks import DiscordHooks

token_ = os.getenv('DISCORD_TOKEN')

hooks = DiscordHooks()
hooks.connect(token_)
