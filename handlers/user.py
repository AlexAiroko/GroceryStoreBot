from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON_RU

from keyboards.store_menu import user_kb_builder

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
	await message.answer(text=LEXICON_RU["start"])


@user_router.message(Command(commands="menu"))
async def process_menu_command(message: Message):
	await message.answer(
		text=LEXICON_RU["menu_user"],
		reply_markup=user_kb_builder.as_markup()
	)


@user_router.callback_query(F.data == "catalogue")
async def process_catalogue_button_pressed(callback: CallbackQuery):
	pass


@user_router.callback_query(F.data == "shopping_cart")
async def process_shopping_cart_button_pressed(callback: CallbackQuery):
	pass


@user_router.callback_query(F.data == "order_status")
async def process_order_status_button_pressed(callback: CallbackQuery):
	pass


@user_router.message()
async def answer_other_message(message: Message):
	await message.answer(LEXICON_RU["other"])