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

#cloudinaryを使うため、コメントアウト
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# Cloudinary の低レベル API やテンプレートタグで設定が必要な場合は以下を有効にする
import cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
cloudinary.config(
    cloud_name=config('CLOUDINARY_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET'),
)
#Ckeditorの画像アップロード先を指定(これがないとうまくいかない)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}



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


# その他の設定があればここに追加
