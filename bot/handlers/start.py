from datetime import datetime
from aiogram.fsm.context import FSMContext
from aiogram import types
from asgiref.sync import sync_to_async
from bot.loader import dp
from aiogram.filters.command import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from index.models import User


@dp.message(CommandStart())
async def main(message: Message, state: FSMContext):
    user_id = message.from_user.id
    obj, created = await User.objects.aget_or_create(id=user_id)
    if created:
        if message.from_user.username:
         obj.full_name = message.from_user.full_name + "(" + message.from_user.username + ")"
        else:
         obj.full_name = message.from_user.full_name
        obj.date_of_birth = datetime.now()
        await obj.asave()
    inline_kb = InlineKeyboardBuilder()
    web_app_info = WebAppInfo(url=f"https://lamprey-romantic-albacore.ngrok-free.app/{user_id}")
    inline_kb.add(types.InlineKeyboardButton(
        text="Launch Axion",
        web_app=web_app_info))
    await message.answer(f'''
    Hey , <b>{message.from_user.full_name}</b>! IT'S Axion!🌟 Your go-to app for crypto trading - all the cool coins and tokens, right in your pocket!📱
    Now we're rolling out our Telegram mini app! Start farming points now, and who knows what cool stuff you'll snag with them soon! 🚀
    Got friends? Bring 'em in! The more, the merrier! 🌱
    Remember: Axion is where growth thrives and endless opportunities bloom! 🌼
    ''', reply_markup=inline_kb.as_markup())

