import random

from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from bot.keyboards import (
    breed_menu,
    count_menu,
    random_again_button,
)
from bot.services.cat_api import fetch_cats
from bot.texts import CAPTIONS


router = Router()


@router.callback_query(F.data == "random")
async def random_cat(callback: CallbackQuery) -> None:
    """Отправляет случайную фотографию кошки"""
    await callback.answer()

    cats = await fetch_cats()

    if not cats:
        await callback.message.answer("Не удалось найти котика 😿")
        return

    await callback.message.answer_photo(
        photo=cats[0]["url"],
        caption="Вот случайный котик 🐱",
        reply_markup=random_again_button()
    )


@router.callback_query(F.data == "count")
async def show_count_menu(callback: CallbackQuery) -> None:
    """Предлагает выбрать количество фотографий"""
    await callback.message.edit_text(
        "Сколько котов показать?",
        reply_markup=count_menu()
    )
    await callback.answer()


@router.callback_query(F.data.startswith("count_"))
async def send_multiple_cats(callback: CallbackQuery) -> None:
    """Отправляет подборку фотографий кошек"""
    count = int(callback.data.split("_")[1])
    await callback.answer()

    cats = await fetch_cats(limit=count)

    if not cats:
        await callback.message.answer("Не удалось найти котиков 😿")
        return

    caption = random.choice(CAPTIONS)

    media = [
        InputMediaPhoto(
            media=cat["url"],
            caption=caption if index == 0 else None,
        )
        for index, cat in enumerate(cats)
    ]

    await callback.message.answer_media_group(media)


@router.callback_query(F.data == "breeds")
async def show_breeds(callback: CallbackQuery) -> None:
    """Показывает меню выбора породы"""
    await callback.message.edit_text(
        "Выбери породу:",
        reply_markup=breed_menu()
    )
    await callback.answer()


@router.callback_query(F.data.startswith("breed_"))
async def send_breed_cat(callback: CallbackQuery) -> None:
    """Отправляет фотографию выбранной породы"""
    breed_id = callback.data.removeprefix("breed_")
    await callback.answer()

    cats = await fetch_cats(breed=breed_id)

    if not cats:
        await callback.message.answer(
            "Не удалось найти фотографии этой породы 😿"
        )
        return

    await callback.message.answer_photo(
        photo=cats[0]["url"],
        caption=f"Порода: {breed_id}"
    )


@router.callback_query(F.data == "info")
async def cat_with_info(callback: CallbackQuery) -> None:
    """Отправляет фотографию кошки и описание ее породы"""
    await callback.answer()

    cats = await fetch_cats(has_breeds=1)

    if not cats or not cats[0].get("breeds"):
        await callback.message.answer(
            "Не удалось найти котика с описанием 😿"
        )
        return

    cat = cats[0]
    breed = cat["breeds"][0]

    caption = (
        f"🐱 <b>{breed.get('name', 'Неизвестная порода')}</b>\n"
        f"🌍 Страна: {breed.get('origin', 'Неизвестно')}\n"
        f"🎭 Характер: {breed.get('temperament', 'Неизвестно')}\n"
        f"⏳ Живут: {breed.get('life_span', 'Неизвестно')} лет"
    )

    await callback.message.answer_photo(
        photo=cat["url"],
        caption=caption
    )
