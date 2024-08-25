from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from filters.admin import IsAdmin

from keyboards.store_menu import admin_menu_kb

from lexicon.lexicon import LEXICON_RU

admin_router = Router()

admin_router.message.filter(IsAdmin())


@admin_router.message(Command(commands="menu"))
async def process_menu_command(message: Message):
	await message.answer(
		text=LEXICON_RU["menu_admin"],
		reply_markup=admin_menu_kb
	)