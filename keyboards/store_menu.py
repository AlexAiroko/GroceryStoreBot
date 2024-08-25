from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


user_kb_builder = InlineKeyboardBuilder()
admin_admin_kb_builder = InlineKeyboardBuilder()
admin_user_kb_builder = InlineKeyboardBuilder()

user_buttons = [
	InlineKeyboardButton(text=LEXICON_RU[text], callback_data=text) for text in ("catalogue", "shopping_cart", "order_status")
]

admin_buttons = [
	InlineKeyboardButton(text=LEXICON_RU[text], callback_data=text) for text in ("setting_catalogue", "setting_category", "questions")
]

change_mode_button = InlineKeyboardButton(text=LEXICON_RU["change_mode"], callback_data="change_mode")


user_kb_builder.row(*user_buttons, width=1)
admin_admin_kb_builder.row(*admin_buttons, change_mode_button, width=2)
admin_user_kb_builder.row(*user_buttons, change_mode_button, width=2)
