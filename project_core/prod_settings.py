import os
import environ
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


DEBUG = False


env = environ.Env()

environ.Env.read_env()

DATABASES = {
    'default': env.db('DATABASE_URL1', default='sqlite:///:memory:'),
    'voter_db': env.db('DATABASE_URL2', default='sqlite:///:memory:'),
}

DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
DATABASES['voter_db']['OPTIONS'] = {'sslmode': 'require'}

CSRF_COOKIE_SECURE  = True

CSRF_COOKIE_PATH = '/'