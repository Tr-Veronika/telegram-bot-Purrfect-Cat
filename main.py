import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from bot.config import BOT_TOKEN, PROXY_URL
from bot.handlers import start_router, cats_router


async def main() -> None:
    """Создает бота и запускает обработку обновлений"""
    session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else None

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=session,
    )

    dp = Dispatcher()
    dp.include_routers(start_router, cats_router)

    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Помощь"),
    ]

    try:
        await bot.set_my_commands(commands)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "[%(asctime)s] #%(levelname)-8s "
            "%(filename)s:%(lineno)d - %(name)s - %(message)s"
        ),
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
