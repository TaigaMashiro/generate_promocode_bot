import asyncio
import asyncpg
from config import DB_USER, DB_NAME, DB_PASSWORD


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host='127.0.0.1',
                port='5432',
            )
        )

    async def add_user(self, user_id: int, first_name: str, username: str, language: str) -> None:
        """Добавить пользователя в базу данных"""
        await self.pool.execute('INSERT INTO users(user_id, first_name, username, language, admin)'
                                'VALUES($1, $2, $3, $4, 0);', user_id, first_name, username, language)

    async def check_user(self, user_id: int) -> bool:
        """Проверить пользователя на наличие в базе данных"""
        response = await self.pool.fetchrow("SELECT user_id FROM users WHERE user_id= $1", user_id)
        if response:
            return True
        else:
            return False

    async def switch_language(self, user_id: int, language: str) -> None:
        await self.pool.execute("UPDATE Users SET language = $2 WHERE user_id = $1", user_id, language)

    async def check_language(self, user_id: int) -> str:
        response = await self.pool.fetchrow("SELECT language FROM users WHERE user_id= $1", user_id)
        if response:
            return response[0]

