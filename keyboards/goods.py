from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.requests import get_categories, get_category_items

from lexicon.lexicon import LEXICON_RU


# kb that show list of categories
async def categories_inline_kb() -> InlineKeyboardMarkup:
	categories = await get_categories()

	kb_builder = InlineKeyboardBuilder()

	for category in categories:
		category_button = InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}")
		kb_builder.add(category_button)
	return kb_builder.adjust(2).as_markup()


# kb that show list of items by category
async def items_inline_kb(category_id: int | str) -> InlineKeyboardMarkup:
	items = await get_category_items(category_id)
	
	kb_builder = InlineKeyboardBuilder()
	
	for item in items:
		item_button = InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}")
		kb_builder.add(item_button)

	kb_builder.add(InlineKeyboardButton(text=LEXICON_RU["categories"], callback_data="catalogue"))

	return kb_builder.adjust(1).as_markup()


# Returns kb with add to cart button
async def add_to_cart_kb(item_id: int | str, count: int = 1) -> InlineKeyboardMarkup:
	return InlineKeyboardMarkup(
		inline_keyboard=[
			[
				InlineKeyboardButton(text="<<", callback_data=f"reduce_{count}_item_{item_id}"),
				InlineKeyboardButton(text=f"{count}", callback_data="item_count"),
				InlineKeyboardButton(text=">>", callback_data=f"increase_{count}_item_{item_id}")
			],
			[InlineKeyboardButton(text=LEXICON_RU["to_cart"], callback_data=f"to_cart_item_{item_id}_{count}")]
		]
	)


async def buy_cart_kb():
	pass