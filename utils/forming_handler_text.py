from db.requests import get_cart

from lexicon.lexicon import LEXICON_RU


async def form_cart(user_id: int) -> str:
	raw_cart = await get_cart(user_id)
	if raw_cart:
		items = raw_cart.split()
		cart = ""
		total_cost = 0
		for item in items:
			name, count, units, price = item.split(":")
			cart += f"{name} - {count} {units} ({price} {LEXICON_RU["currency"]})\n"
			total_cost += int(price)
		cart += f"\n{LEXICON_RU["total_cost"]}: {total_cost} {LEXICON_RU["currency"]}"
	else:
		cart = LEXICON_RU["empty_cart"]
	return cart