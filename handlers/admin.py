import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

from filters.admin import IsAdmin

from keyboards.store_menu import admin_admin_kb_builder, admin_user_kb_builder

from lexicon.lexicon import LEXICON_RU


logger = logging.getLogger(__name__)

admin_router = Router()

admin_router.message.filter(IsAdmin())


@admin_router.message(Command(commands="menu"))
async def process_menu_command(message: Message):
	await message.answer(
		text=LEXICON_RU["menu_admin"],
		reply_markup=admin_admin_kb_builder.as_markup()
	)


@admin_router.callback_query(F.data == "change_mode")
async def process_menu_command(callback: CallbackQuery):
	# Compare Inline Keyboards from message and from kb builder through first button text
	if callback.message.reply_markup.inline_keyboard[0][0].text == admin_admin_kb_builder.as_markup().inline_keyboard[0][0].text:
		await callback.message.edit_reply_markup(
			reply_markup=admin_user_kb_builder.as_markup()
		)
	else:
		await callback.message.edit_reply_markup(
			reply_markup=admin_admin_kb_builder.as_markup()
		)