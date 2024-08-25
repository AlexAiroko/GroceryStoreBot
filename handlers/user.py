from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from lexicon.lexicon import LEXICON_RU


user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
	await message.answer(text=LEXICON_RU["start"])
