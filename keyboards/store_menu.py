from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


USER_BUTTONS = [
	InlineKeyboardButton(text=LEXICON_RU[text], callback_data=text) for text in ("catalogue", "shopping_cart", "order_status")
]

ADMIN_BUTTONS = [
	InlineKeyboardButton(text=LEXICON_RU[text], callback_data=text) for text in ("setting_catalogue", "orders", "questions")
]

CHANGE_MODE_BUTTON = InlineKeyboardButton(text=LEXICON_RU["change_mode"], callback_data="change_mode")


def get_user_kb() -> InlineKeyboardMarkup:
	user_kb_builder = InlineKeyboardBuilder()
	user_kb_builder.row(*USER_BUTTONS, width=1)

	return user_kb_builder.as_markup()

def get_admin_admin_kb() -> InlineKeyboardMarkup:
	admin_admin_kb_builder = InlineKeyboardBuilder()
	admin_admin_kb_builder.row(*ADMIN_BUTTONS, CHANGE_MODE_BUTTON, width=2)

	return admin_admin_kb_builder.as_markup()


def get_admin_user_kb() -> InlineKeyboardMarkup:
	admin_user_kb_builder = InlineKeyboardBuilder()
	admin_user_kb_builder.row(*USER_BUTTONS, CHANGE_MODE_BUTTON, width=2)

	return admin_user_kb_builder.as_markup()
