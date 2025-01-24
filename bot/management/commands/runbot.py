import asyncio
from django.core.management.base import BaseCommand
from bot.handlers import *
from bot.loader import bot, dp
from bot.utils.set_bot_commands import set_default_commands


async def main():
    await set_default_commands(bot)
    await dp.start_polling(bot)


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        asyncio.run(main())
