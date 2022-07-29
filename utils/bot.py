import aiosqlite
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands

from utils.http import HTTPSession
from utils.config import Config
from utils.CONSTANTS import __VERSION__

with open("setup.sql", "r") as sql_file:
    SETUP_SQL = sql_file.read()


class OGIROID(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.db = None
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.session = HTTPSession(loop=self.loop)
        self.commands_ran = {}
        self.total_commands_ran = 0

    async def on_command(self, ctx):
        self.total_commands_ran += 1
        try:
            self.commands_ran[ctx.command.qualified_name] += 1
        except KeyError:
            self.commands_ran[ctx.command.qualified_name] = 1

    async def on_slash_command(self, inter: ApplicationCommandInteraction):
        self.total_commands_ran += 1
        try:
            self.commands_ran[inter.application_command.name] += 1
        except KeyError:
            self.commands_ran[inter.application_command.name] = 1

    async def on_ready(self):
        await self.wait_until_ready()
        await self.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="the users!"))
        for command in self.application_commands:
            self.commands_ran[f'{command.qualified_name}'] = 0
        print("--------------------------------------------------------------------------------")
        print("Bot is ready! Logged in as: " + self.user.name)
        print("Bot devs: HarryDaDev | FreebieII | JasonLovesDoggo | Levani | DWAA")
        print(f"Bot version: {__VERSION__}")
        print("--------------------------------------------------------------------------------")

    async def start(self, *args, **kwargs):
        async with aiosqlite.connect("data.db") as self.db:
            await self.db.executescript(SETUP_SQL)
            await super().start(*args, **kwargs)
