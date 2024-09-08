from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON_RU

from keyboards.store_menu import get_user_kb
from keyboards.goods import categories_inline_kb, items_inline_kb, add_to_cart_kb

from db.requests import set_user, get_item, add_to_cart

from utils.forming_handler_text import form_cart


user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
	await set_user(message.from_user.id)
	await message.answer(text=LEXICON_RU["start"])


@user_router.message(Command(commands="menu"))
async def process_menu_command(message: Message):
	await message.answer(
		text=LEXICON_RU["menu_user"],
		reply_markup=get_user_kb()
	)


@user_router.message(Command(commands="help"))
async def process_menu_command(message: Message):
	await message.answer(text=LEXICON_RU["help"])


@user_router.callback_query(F.data == "catalogue")
async def process_catalogue_button_pressed(callback: CallbackQuery):
	await callback.message.edit_text(
		text=LEXICON_RU["categories"],
		reply_markup=await categories_inline_kb()
	)
	await callback.answer()


@user_router.callback_query(F.data.startswith('category_'))
async def process_category_button_pressed(callback: CallbackQuery):
	
	await callback.message.edit_text(
		text=LEXICON_RU['items'],
		reply_markup=await items_inline_kb(callback.data.split("_")[-1])
	)


@user_router.callback_query(F.data.startswith('item_'))
async def process_item_button_pressed(callback: CallbackQuery):
	item_id = callback.data.split("_")[-1]
	item_data = await get_item(item_id)
	await callback.answer('Вы выбрали товар')
	await callback.message.answer(
		text=f"{item_data.name}\n"
			f"{LEXICON_RU["description"]}: {item_data.description}\n"
			f"{LEXICON_RU["price"]}: {item_data.price} {LEXICON_RU["currency"]}/{item_data.units}\n\n"
			f"{LEXICON_RU["select_items_count"]}",
		reply_markup=await add_to_cart_kb(item_id)
	)


@user_router.callback_query(F.data.startswith('reduce_'))
async def process_reduce_button_pressed(callback: CallbackQuery):
	item_id = callback.data.split("_")[-1]
	count = int(callback.data.split("_")[1])
	if count > 1:
		await callback.message.edit_reply_markup(
			reply_markup=await add_to_cart_kb(item_id, count - 1)
		)
	await callback.answer()


@user_router.callback_query(F.data.startswith('increase_'))
async def process_increase_button_pressed(callback: CallbackQuery):
	item_id = callback.data.split("_")[-1]
	count = int(callback.data.split("_")[1])
	await callback.message.edit_reply_markup(
		reply_markup=await add_to_cart_kb(item_id, count + 1)
	)
	await callback.answer()


@user_router.callback_query(F.data.startswith('to_cart_item_'))
async def process_item_button_pressed(callback: CallbackQuery):
	item_id = int(callback.data.split("_")[-2])
	count = int(callback.data.split("_")[-1])
	
	await add_to_cart(item_id, count, callback.from_user.id)
	await callback.message.answer(LEXICON_RU["item_was_added"])
	await callback.answer()



@user_router.callback_query(F.data == "shopping_cart")
async def process_shopping_cart_button_pressed(callback: CallbackQuery):
	cart = await form_cart(callback.from_user.id)
	if cart != LEXICON_RU["empty_cart"]:
		await callback.message.answer(
			text=cart
		)
	else:
		await callback.message.answer(cart)
	await callback.answer()


@user_router.callback_query(F.data == "order_status")
async def process_order_status_button_pressed(callback: CallbackQuery):
	pass


@user_router.message()
async def answer_other_message(message: Message):
	await message.answer(LEXICON_RU["other"])