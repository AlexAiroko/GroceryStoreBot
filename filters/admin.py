from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):
	def __init__(self) -> None:
		super().__init__()

	async def __call__(self, message: Message, admin_ids: list[int]) -> bool:
		return message.from_user.id in admin_ids