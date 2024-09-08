import logging

from .models import async_session
from .models import User, Category, Item, Question, Order

from sqlalchemy import ScalarResult, select, update


logger = logging.getLogger(__name__)


async def set_user(tg_id: int) -> None:
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))

		if not user:
			session.add(User(tg_id=tg_id, cart="", order_status=""))
			await session.commit()


async def get_categories() -> ScalarResult[Category]:
	async with async_session() as session:
		logging.info(type(await session.scalars(select(Category))))
		return await session.scalars(select(Category))


async def get_category_items(category_id: int) -> ScalarResult[Item]:
	async with async_session() as session:
		return await session.scalars(select(Item).where(Item.category == category_id))


async def get_item(item_id: int) -> Item:
	async with async_session() as session:
		logging.info(type(await session.scalar(select(Item).where(Item.id == item_id))))
		return await session.scalar(select(Item).where(Item.id == item_id))


async def add_to_cart(item_id: int, count: int, tg_id: int) -> None:
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))
		item = await session.scalar(select(Item).where(Item.id == item_id))
		if item.name in user.cart:
			goods = user.cart.split()
			for ind, goods_one in enumerate(goods):
				if item.name in goods_one:
					fields = goods_one.split(":")
					fields[1] = str(int(fields[1]) + count)
					fields[3] = str(int(fields[3]) + count * item.price)
					goods_one = ":".join(fields)
					break
			goods[ind] = goods_one
			user.cart = " ".join(goods)
		elif user.cart:
			user.cart += f" {item.name}:{count}:{item.units}:{item.price * count}"
		else:
			user.cart = f"{item.name}:{count}:{item.units}:{item.price * count}"
		await session.commit()


async def get_cart(tg_id: int) -> str:
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))
		return user.cart