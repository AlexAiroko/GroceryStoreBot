import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

from filters.admin import IsAdmin

from keyboards.store_menu import get_admin_admin_kb, get_admin_user_kb

from lexicon.lexicon import LEXICON_RU


logger = logging.getLogger(__name__)

admin_router = Router()

admin_router.message.filter(IsAdmin())


@admin_router.message(Command(commands="menu"))
async def process_menu_command(message: Message):
	await message.answer(
		text=LEXICON_RU["menu_admin"],
		reply_markup=get_admin_admin_kb()
	)


@admin_router.callback_query(F.data == "setting_catalogue")
async def process_setting_catalogue_button_pressed(callback: CallbackQuery):
	pass


@admin_router.callback_query(F.data == "orders")
async def process_orders_button_pressed(callback: CallbackQuery):
	pass


@admin_router.callback_query(F.data == "questions")
async def process_questions_button_pressed(callback: CallbackQuery):
	pass



@admin_router.callback_query(F.data == "change_mode")
async def process_change_mode_button_pressed(callback: CallbackQuery):
	# Compare Inline Keyboards from message and from kb builder through first button text
	if callback.message.reply_markup.inline_keyboard[0][0].text == get_admin_admin_kb().inline_keyboard[0][0].text:
		await callback.message.edit_reply_markup(
			reply_markup=get_admin_user_kb()
		)
	else:
		await callback.message.edit_reply_markup(
			reply_markup=get_admin_admin_kb()
		)