from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU

# Создаем клавиатуру в кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb.add(button_yes, button_no)
yes_no_kb.adjust(2)

# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
game_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

game_kb.add(button_1).add(button_2).add(button_3)
