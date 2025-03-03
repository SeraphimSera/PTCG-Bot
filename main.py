import discord
import os
from dotenv import load_dotenv


load_dotenv()

class PTCGBot(discord.Bot):
    # load cogs here?
    # it's been a while i don't remember much
    pass


bot = PTCGBot()
bot.run(os.getenv('DISCORD_TOKEN'))