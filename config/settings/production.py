# config/settings/production.py

from .base import *
from decouple import Config, RepositoryEnv
import dj_database_url
import django_heroku

# .env.prod ファイルを指定して読み込む
env_path = BASE_DIR / 'secrets' / '.env.prod'
config = Config(RepositoryEnv(str(env_path)))

# 環境変数の取得
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
STRIPE_API_SECRET_KEY = config('STRIPE_API_SECRET_KEY')
MY_URL = config('MY_URL')

# データベース設定（Heroku の PostgreSQL を使用）
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# WhiteNoise の設定
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Heroku の設定
django_heroku.settings(locals())

# セキュリティ設定
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# 静的ファイルの設定
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# その他の設定があればここに追加
