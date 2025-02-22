# config/settings/production.py

from .base import *
# from decouple import Config, RepositoryEnv
import dj_database_url

# # .env.prod ファイルを指定して読み込む
# env_path = BASE_DIR / 'secrets' / '.env.prod'
# config = Config(RepositoryEnv(str(env_path)))

# # 環境変数の取得
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
# STRIPE_API_SECRET_KEY = config('STRIPE_API_SECRET_KEY')
# MY_URL = config('MY_URL')

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
STRIPE_API_SECRET_KEY = os.environ.get('STRIPE_API_SECRET_KEY')
MY_URL = os.environ.get('MY_URL')

# データベース設定（Heroku の PostgreSQL を使用）
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'qj_ecsite-dev.onrender.com').split(',')

# WhiteNoise の設定
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# セキュリティ設定
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# # 静的ファイルの設定
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# その他の設定があればここに追加
