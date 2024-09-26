# config/settings/development.py

from .base import *
from decouple import Config, RepositoryEnv

# .env.dev ファイルを指定して読み込む
env_path = BASE_DIR / 'secrets' / '.env.dev'
config = Config(RepositoryEnv(str(env_path)))

# 環境変数の取得
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
STRIPE_API_SECRET_KEY = config('STRIPE_API_SECRET_KEY')
MY_URL = config('MY_URL')

# データベース設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# 静的ファイルの設定
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# その他の設定があればここに追加
