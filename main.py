import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import Config, load_config

from handlers.user import user_router
from handlers.admin import admin_router
from handlers.other import other_router

from keyboards.main_menu import set_main_menu


# Logger initialization
logger = logging.getLogger(__name__)


async def main() -> None:
	# Config Logger
	logging.basicConfig(
		level=logging.DEBUG,
		format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
	)
	
	logger.info('Starting Bot')

	# Load config
	config: Config = load_config(".env")

	# Bot and Dispatcher initialization
	bot = Bot(
		token=config.tg_bot.token,
		default=DefaultBotProperties(parse_mode=ParseMode.HTML)
	)
	dp = Dispatcher()

	# Admins list
	admin_ids = config.tg_bot.admin_ids
	dp.workflow_data.update({'admin_ids': admin_ids})

	# Setting main menu
	await set_main_menu(bot)
	
	# Register Routers
	dp.include_router(admin_router)
	dp.include_router(user_router)
	dp.include_router(other_router)
	
	# Start polling
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


# Running main
if __name__ == "__main__":
	asyncio.run(main())