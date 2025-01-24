from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from django.conf import settings


bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
