from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

other_router = Router()


@other_router.message()
async def answer_other_message(message: Message):
	await message.answer(LEXICON_RU["other"])