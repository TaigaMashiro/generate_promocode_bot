import os
from dotenv import load_dotenv

BASEDIR = os.path.dirname(os.path.realpath('main.py'))

dotenv_path = os.path.join(BASEDIR, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


TOKEN = os.environ.get('TELEGRAM_TOKEN')
IM_PATH = os.environ.get('IM_PATH')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
