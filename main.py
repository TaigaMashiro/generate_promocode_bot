from aiogram.utils import executor
from bot import dp, bot
from utils.database import create_table_db
from handlers import client


async def bot_start(_):
    await create_table_db.run()
    bot_info = await bot.get_me()
    print(f'Телеграм бот "{bot_info.first_name}" успешно запущен!')


async def bot_stop(_):
    print('Бот выключен')


client.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start, on_shutdown=bot_stop)
