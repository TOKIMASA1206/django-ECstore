# config/settings/production.py

from .base import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
STRIPE_API_SECRET_KEY = os.environ.get('STRIPE_API_SECRET_KEY')
MY_URL = os.environ.get('MY_URL')

# データベース設定
# Render の環境変数から取得
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'qj_ecsite-dev.onrender.com').split(',')

# WhiteNoise の設定
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary の設定
import cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
)
#Ckeditorの画像アップロード先を指定(これがないとうまくいかない)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# セキュリティ設定
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# その他の設定があればここに追加
