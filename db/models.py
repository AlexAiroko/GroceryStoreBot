from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
	pass


class User(Base):
	__tablename__ = 'users'

	id: Mapped[int] = mapped_column(primary_key=True)
	tg_id = mapped_column(BigInteger)
	cart: Mapped[str] = mapped_column(String(200))
	order_status: Mapped[str] = mapped_column(String(50))


class Category(Base):
	__tablename__ = 'categories'

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(25))


class Item(Base):
	__tablename__ = 'items'

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(25))
	description: Mapped[str] = mapped_column(String(120))
	price: Mapped[int] = mapped_column()
	units: Mapped[str] = mapped_column(String(10))
	category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class Question(Base):
	__tablename__ = 'questions'

	id: Mapped[int] = mapped_column(primary_key=True)
	text: Mapped[str] = mapped_column(String(250))


class Order(Base):
	__tablename__ = 'orders'

	id: Mapped[int] = mapped_column(primary_key=True)
	tg_id = mapped_column(BigInteger)
	username: Mapped[str] = mapped_column(String(50))
	address: Mapped[str] = mapped_column(String(100))


async def create_tables() -> None:
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)