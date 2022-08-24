from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import Throttled

import gc

from bot import bot, db, dp
from keybroads.client import (
    select_language_kb, switch_generate_photo_ru_kb, switch_generate_photo_uz_kb, comeback_ru_kb, comeback_uz_kb
)

from utils.scripts.generate_params import output_params
from utils.scripts.create_files import create_image, create_video

import os


class Generate(StatesGroup):
    generate_file = State()
    generate_photo = State()
    generate_video = State()


async def command_start(message: types.Message):
    user_id = message.from_user.id
    try:
        await dp.throttle('start', rate=3)
    except Throttled:
        await bot.send_message(user_id, 'Не флудите!')
    else:
        if await db.check_user(user_id):
            await bot.send_message(user_id,
                                   "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                   "Здравствуйте, я бот для генерации промокодов. Выберите язык. 🇷🇺\n"
                                   "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                   "Asslomu alaykum, men promokodlarni yaratadigan bot. Tilni tanlang. 🇺🇿",
                                   reply_markup=select_language_kb)
        else:
            await db.add_user(user_id, message.from_user.first_name, message.from_user.username, 'ru')
            await bot.send_message(user_id,
                                   "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                   "Здравствуйте, я бот для генерации промокодов. Выберите язык. 🇷🇺\n"
                                   "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                   "Asslomu alaykum, men promokodlarni yaratadigan bot. Tilni tanlang. 🇺🇿",
                                   reply_markup=select_language_kb)


async def choose_language(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                           "Здравствуйте, я бот для генерации промокодов. Выберите язык. 🇷🇺\n"
                           "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                           "Asslomu alaykum, men promokodlarni yaratadigan bot. Tilni tanlang. 🇺🇿",
                           reply_markup=select_language_kb)


async def switch_language_to_ru_or_uz(message: types.Message):
    user_id = message.from_user.id
    print(message.text)
    if message.text == 'Русский 🇷🇺':
        language = 'ru'
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Выбран русский язык. 🇷🇺\n"
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Выберите через клавиатуру в каком виде хотите получить промокод ⬇️",
                               reply_markup=switch_generate_photo_ru_kb)
    else:
        language = 'uz'
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Oʻzbek tili tanlangan. 🇺🇿\n"
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodni qaysi shaklda olishni xohlayotganingizni klaviatura orqali tanlang ⬇️",
                               reply_markup=switch_generate_photo_uz_kb)
    await db.switch_language(user_id, language)


async def generate_photo_as_file(message: types.Message):
    user_id = message.from_user.id
    check_language = await db.check_language(user_id)
    if check_language == 'ru':
        await bot.send_message(message.from_user.id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Введите текст от 1 до 13 символов, которые хотите сгенерировать в промокоде. ⬇️\n",
                               reply_markup=comeback_ru_kb)
    else:
        await bot.send_message(message.from_user.id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodda yaratmoqchi bo'lgan 1 dan 13 gacha harflar yoki "
                               "raqamlardan iborat so'zni kiriting.. ⬇️\n",
                               reply_markup=comeback_uz_kb)
    await Generate.generate_file.set()


async def generate_video(message: types.Message):
    user_id = message.from_user.id
    check_language = await db.check_language(user_id)
    if check_language == 'ru':
        await bot.send_message(message.from_user.id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Введите текст от 1 до 13 символов, которые хотите сгенерировать в промокоде. ⬇️\n",
                               reply_markup=comeback_ru_kb)
    else:
        await bot.send_message(message.from_user.id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodda yaratmoqchi bo'lgan 1 dan 13 gacha harflar yoki "
                               "raqamlardan iborat so'zni kiriting.. ⬇️\n",
                               reply_markup=comeback_uz_kb)
    await Generate.generate_video.set()


async def generate_photo_as_photo(message: types.Message):
    user_id = message.from_user.id
    check_language = await db.check_language(user_id)
    if check_language == 'ru':
        await bot.send_message(message.from_user.id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Введите текст от 1 до 13 символов, которые хотите сгенерировать в промокоде. ⬇️\n",
                               reply_markup=comeback_ru_kb)
    else:
        await bot.send_message(message.from_user.id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodda yaratmoqchi bo'lgan 1 dan 13 gacha harflar yoki "
                               "raqamlardan iborat so'zni kiriting.. ⬇️\n",
                               reply_markup=comeback_uz_kb)
    await Generate.generate_photo.set()


async def send_generate_photo(message: types.Message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    if text == 'Назад':
        await state.finish()
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Выберите через клавиатуру в каком виде хотите получить промокод ⬇️",
                               reply_markup=switch_generate_photo_ru_kb)
    elif text == 'Orqaga':
        await state.finish()
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodni qaysi shaklda olishni xohlayotganingizni klaviatura orqali tanlang ⬇️",
                               reply_markup=switch_generate_photo_uz_kb)
    else:
        try:
            await dp.throttle('throttling_file', rate=150)
        except Throttled:
            await bot.send_message(user_id, 'Дождитесь окнончания генерации ваших промокодов!')
        else:
            check_language = await db.check_language(user_id)
            if check_language == 'ru':
                if len(text) >= 14:
                    await bot.send_message(user_id, '❌ Максимальный допустимый ввод символов 13!')
                else:
                    await state.finish()
                    get_params = output_params(text)
                    get_amount_files = os.listdir(
                        os.path.join(
                            os.path.dirname(os.path.realpath('main.py')), 'data', 'images', 'compressed', 'ru')
                    )
                    number = 0
                    message_progress = await bot.send_message(user_id, f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                                       f'\n❕Началась генерация промокодов!'
                                                                       f'\n♻️Прогресс {number}/{len(get_amount_files)}')
                    for file in get_amount_files:
                        file_path = os.path.join(os.path.dirname(
                            os.path.realpath('main.py')), 'data', 'images', 'compressed', 'ru', file
                        )
                        create_img = create_image(file_path, get_params['coordinate'], get_params['font_size'], text,
                                                  number, 32)
                        number += 1
                        await bot.edit_message_text(f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                    f'\n❕Началась генерация промокодов!'
                                                    f'\n♻️Прогресс {number}/{len(get_amount_files)}', user_id,
                                                    message_progress.message_id)
                        await message.reply_photo(open(create_img, 'rb'))
                        os.remove(create_img)
                        gc.collect()

                    await bot.send_message(user_id, '♻ Генерация промокодов завершена!',
                                           reply_markup=switch_generate_photo_ru_kb)
            elif check_language == 'uz':
                if len(text) >= 14:
                    await bot.send_message(user_id, '❌ Maksimal ruxsat etilgan belgilar kiritish - 13!')
                else:
                    get_params = output_params(text)
                    get_amount_files = os.listdir(
                        os.path.join(
                            os.path.dirname(os.path.realpath('main.py')), 'data', 'images', 'not_compressed', 'uz')
                    )
                    number = 0
                    message_progress = await bot.send_message(user_id, f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                                       f'\n❕Promokodlar yaratish boshlandi!'
                                                                       f'\n♻️Taraqqiyot {number}/{len(get_amount_files)}')
                    for file in get_amount_files:
                        file_path = os.path.join(os.path.dirname(
                            os.path.realpath('main.py')), 'data', 'images', 'not_compressed', 'uz', file
                        )
                        create_img = create_image(file_path, get_params['coordinate'], get_params['font_size'], text,
                                                  number, 32)
                        number += 1
                        await bot.edit_message_text(f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                    f'\n❕Promokodlar yaratish boshlandi!'
                                                    f'\n♻️Taraqqiyot {number}/{len(get_amount_files)}', user_id,
                                                    message_progress.message_id)
                        await message.reply_photo(open(create_img, 'rb'))
                        os.remove(create_img)
                        gc.collect()
                    await state.finish()
                    await bot.send_message(user_id, '♻ Генерация промокодов завершена!',
                                           reply_markup=switch_generate_photo_uz_kb)


async def send_generate_file(message: types.Message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    if text == 'Назад':
        await state.finish()
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Выберите через клавиатуру в каком виде хотите получить промокод ⬇️",
                               reply_markup=switch_generate_photo_ru_kb)
    elif text == 'Orqaga':
        await state.finish()
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodni qaysi shaklda olishni xohlayotganingizni klaviatura orqali tanlang ⬇️",
                               reply_markup=switch_generate_photo_uz_kb)
    else:
        try:
            await dp.throttle('throttling_file', rate=150)
        except Throttled:
            await bot.send_message(user_id, 'Дождитесь окнончания генерации ваших промокодов!')
        else:
            check_language = await db.check_language(user_id)
            if check_language == 'ru':
                if len(text) >= 14:
                    await bot.send_message(user_id, '❌ Максимальный допустимый ввод символов 13!')
                else:
                    await state.finish()
                    get_params = output_params(text)
                    get_amount_files = os.listdir(
                        os.path.join(
                            os.path.dirname(os.path.realpath('main.py')), 'data', 'images', 'not_compressed', 'ru')
                    )
                    number = 0
                    message_progress = await bot.send_message(user_id, f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                                       f'\n❕Началась генерация промокодов!'
                                                                       f'\n♻️Прогресс {number}/{len(get_amount_files)}')
                    for file in get_amount_files:
                        file_path = os.path.join(os.path.dirname(
                            os.path.realpath('main.py')), 'data', 'images', 'not_compressed', 'ru', file
                        )
                        create_img = create_image(file_path, get_params['coordinate'], get_params['font_size'], text,
                                                  number, 'black')
                        number += 1
                        await bot.edit_message_text(f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                    f'\n❕Началась генерация промокодов!'
                                                    f'\n♻️Прогресс {number}/{len(get_amount_files)}', user_id,
                                                    message_progress.message_id)
                        await message.reply_document(open(create_img, 'rb'))
                        os.remove(create_img)
                        gc.collect()

                    await bot.send_message(user_id, '♻ Генерация промокодов завершена!',
                                           reply_markup=switch_generate_photo_ru_kb)
            elif check_language == 'uz':
                if len(text) >= 14:
                    await bot.send_message(user_id, '❌ Maksimal ruxsat etilgan belgilar kiritish - 13!')
                else:
                    get_params = output_params(text)
                    get_amount_files = os.listdir(
                        os.path.join(
                            os.path.dirname(os.path.realpath('main.py')), 'data', 'images', 'not_compressed', 'uz')
                    )
                    number = 0
                    message_progress = await bot.send_message(user_id, f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                                       f'\n❕Promokodlar yaratish boshlandi!'
                                                                       f'\n♻️Taraqqiyot {number}/{len(get_amount_files)}')
                    for file in get_amount_files:
                        file_path = os.path.join(os.path.dirname(
                            os.path.realpath('main.py')), 'data', 'images', 'not_compressed', 'uz', file
                        )
                        create_img = create_image(file_path, get_params['coordinate'], get_params['font_size'], text,
                                                  number, 'black')
                        number += 1
                        await bot.edit_message_text(f'➖➖➖➖➖➖➖➖➖➖➖➖➖'
                                                    f'\n❕Promokodlar yaratish boshlandi!'
                                                    f'\n♻️Taraqqiyot {number}/{len(get_amount_files)}', user_id,
                                                    message_progress.message_id)
                        await message.reply_document(open(create_img, 'rb'))
                        os.remove(create_img)
                        gc.collect()
                    await state.finish()
                    await bot.send_message(user_id, '♻ Генерация промокодов завершена!',
                                           reply_markup=switch_generate_photo_uz_kb)


async def send_generate_video(message: types.Message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    if text == 'Назад':
        await state.finish()
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Выберите через клавиатуру в каком виде хотите получить промокод ⬇️",
                               reply_markup=switch_generate_photo_ru_kb)
    elif text == 'Orqaga':
        await state.finish()
        await bot.send_message(user_id,
                               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                               "Promo-kodni qaysi shaklda olishni xohlayotganingizni klaviatura orqali tanlang ⬇️",
                               reply_markup=switch_generate_photo_uz_kb)
    else:
        try:
            await dp.throttle('throttling_file', rate=150)
        except Throttled:
            await bot.send_message(user_id, 'Дождитесь окнончания генерации ваших промокодов!')
        else:
            check_language = await db.check_language(user_id)
            if check_language == 'ru':
                if len(text) >= 14:
                    await bot.send_message(user_id, '❌ Максимальный допустимый ввод символов 13!')
                else:
                    video_path = os.path.join(
                        os.path.dirname(os.path.realpath('main.py')), 'data', 'videos', 'compru.mp4'
                    )
                    video_name = create_video(video_path, text, [0, 4, 4, 6, 6, 29], 950, 2)
                    await message.reply_document(open(video_name + '.mp4', 'rb'))
                    os.remove(video_name + '.mp4')
                    gc.collect()
            elif check_language == 'uz':
                if len(text) >= 14:
                    await bot.send_message(user_id, '❌ Maksimal ruxsat etilgan belgilar kiritish - 13!')
                else:
                    video_path = os.path.join(
                        os.path.dirname(os.path.realpath('main.py')), 'data', 'videos', 'comp.mp4'
                    )
                    video_name = create_video(video_path, text, [0, 10, 10, 14, 14, 29], 990, 4)
                    await message.reply_document(open(video_name + '.mp4', 'rb'))
                    os.remove(video_name + '.mp4')
                    gc.collect()


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start'])

    dispatcher.register_message_handler(choose_language,
                                        content_types=['text'], text=['Tilni tanlang 🇺🇿 🇷🇺', 'Выбрать язык 🇷🇺 🇺🇿'])

    dispatcher.register_message_handler(switch_language_to_ru_or_uz, content_types=['text'], text=['Русский 🇷🇺', "O'zbek tili 🇺🇿"])

    dispatcher.register_message_handler(generate_photo_as_file, content_types=['text'],
                                        text=['Получить в виде файла 📄', 'Fayl sifatida olish 📄'])

    dispatcher.register_message_handler(generate_photo_as_photo, content_types=['text'],
                                        text=['Получить в виде фото 🖼', 'Foto sifatida olish 🖼'])

    dispatcher.register_message_handler(generate_video, content_types=['text'],
                                        text=['Получить в виде ролика 📹', 'Video sifatida olish 📹'])

    dispatcher.register_message_handler(send_generate_file, state=Generate.generate_file)
    dispatcher.register_message_handler(send_generate_photo, state=Generate.generate_photo)
    dispatcher.register_message_handler(send_generate_video, state=Generate.generate_video)
