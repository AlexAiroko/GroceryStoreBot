from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON_RU

from keyboards.store_menu import user_menu_kb

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
	await message.answer(text=LEXICON_RU["start"])


@user_router.message(Command(commands="menu"))
async def process_menu_command(message: Message):
	await message.answer(
		text=LEXICON_RU["menu_user"],
		reply_markup=user_menu_kb
	)


@user_router.message()
async def answer_other_message(message: Message):
	await message.answer(LEXICON_RU["other"])