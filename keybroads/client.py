from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


uzb_language_btn = KeyboardButton("O'zbek tili 🇺🇿")
ru_language_btn = KeyboardButton("Русский 🇷🇺")

select_language_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(uzb_language_btn, ru_language_btn)

generate_photo_output_btn = KeyboardButton('Получить в виде файла 📄')
generate_file_output_btn = KeyboardButton('Получить в виде фото 🖼')
generate_video_output_btn = KeyboardButton('Получить в виде ролика 📹')
switch_language_ru_btn = KeyboardButton('Выбрать язык 🇷🇺 🇺🇿')

switch_generate_photo_ru_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    generate_photo_output_btn
).add(
    generate_file_output_btn
).add(
    generate_video_output_btn
).add(
    switch_language_ru_btn
)


generate_photo_output_uz_btn = KeyboardButton('Fayl sifatida olish 📄')
generate_file_output_uz_btn = KeyboardButton('Foto sifatida olish 🖼')
generate_video_output_uz_btn = KeyboardButton('Video sifatida olish 📹')
switch_language_uz_btn = KeyboardButton('Tilni tanlang 🇺🇿 🇷🇺')

switch_generate_photo_uz_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    generate_photo_output_uz_btn
).add(
    generate_file_output_uz_btn
).add(
    generate_video_output_uz_btn
).add(
    switch_language_uz_btn
)

comeback_ru_kb = ReplyKeyboardMarkup(resize_keyboard=True).add('Назад')
comeback_uz_kb = ReplyKeyboardMarkup(resize_keyboard=True).add('Orqaga')
