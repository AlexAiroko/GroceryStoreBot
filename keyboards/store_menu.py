from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon import LEXICON_RU


user_menu_kb = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text=LEXICON_RU["catalogue"])],
		[KeyboardButton(text=LEXICON_RU["shopping_cart"])],
		[KeyboardButton(text=LEXICON_RU["order_status"])]
	],
	resize_keyboard=True
)

admin_menu_kb = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text=LEXICON_RU["setting_catalogue"])],
		[
			KeyboardButton(text=LEXICON_RU["questions"]),
			KeyboardButton(text=LEXICON_RU["setting_category"])
		]
	],
	resize_keyboard=True
)