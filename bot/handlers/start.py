from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards import main_menu
from bot.texts import HELP_TEXT


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """Отправляет приветствие и главное меню"""
    await message.answer(
        HELP_TEXT,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    """Показывает краткую справку по боту"""
    await message.answer(
        "Используй кнопки под сообщением 👇\n\n"
        "Через них можно выбрать действие бота.",
        reply_markup=main_menu()
    )


@router.callback_query(F.data == "back")
async def back_to_menu(callback: CallbackQuery) -> None:
    """Возвращает пользователя в главное меню"""
    await callback.message.edit_text(
        HELP_TEXT,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )
    await callback.answer()
