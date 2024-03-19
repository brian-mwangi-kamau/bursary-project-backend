import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': os.environ['ENGINE'],
        'NAME': os.environ['default_db_name'],
        'USER': os.environ['default_db_user'],
        'PASSWORD': os.environ['default_db_password'],
        'HOST': os.environ['default_db_host'],
        'PORT': os.environ['default_db_port'],
        'OPTIONS': {'sslmode': 'require'},
    },
    
    'voter_db': {
        'ENGINE': os.environ['ENGINE'],
        'NAME': os.environ['voter_db_name'],
        'USER': os.environ['voter_db_user'],
        'PASSWORD': os.environ['voter_db_password'],
        'HOST': os.environ['voter_db_host'],
        'PORT': os.environ['voter_db_port'],
        'OPTIONS': {'sslmode': 'require'},
    }
}