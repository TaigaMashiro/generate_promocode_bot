from bot import db
from asyncpg.exceptions import DuplicateTableError


async def create_table_users():
    sql = 'CREATE TABLE users(' \
          'user_id bigint PRIMARY KEY, first_name text, username text, language text, admin int);'
    await db.pool.execute(sql)


async def run():
    try:
        await create_table_users()
    except DuplicateTableError as e:
        print(e)
