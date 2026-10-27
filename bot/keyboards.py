from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu() -> InlineKeyboardMarkup:
    """Создает главное меню бота"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🐾 Случайный кот", callback_data="random")],
            [InlineKeyboardButton(text="🧬 Выбрать породу", callback_data="breeds")],
            [InlineKeyboardButton(text="📚 Случайный кот с описанием", callback_data="info")],
            [InlineKeyboardButton(text="🐱 Несколько котов", callback_data="count")],
        ]
    )


def back_button() -> InlineKeyboardMarkup:
    """Создает кнопку возврата в главное меню"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
        ]
    )


def breed_menu() -> InlineKeyboardMarkup:
    """Создает меню выбора породы кошки"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Bengal", callback_data="breed_beng")],
            [InlineKeyboardButton(text="Abyssinian", callback_data="breed_abys")],
            [InlineKeyboardButton(text="Siamese", callback_data="breed_siam")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")],
        ]
    )


def count_menu() -> InlineKeyboardMarkup:
    """Создает меню выбора количества фотографий"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=str(count), callback_data=f"count_{count}")
                for count in range(2, 6)
            ],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")],
        ]
    )


def random_again_button() -> InlineKeyboardMarkup:
    """Создает кнопку для получения следующего котика"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🐾 Ещё котик", callback_data="random")]
        ]
    )