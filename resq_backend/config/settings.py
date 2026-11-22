from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='dev-only-resq-key'
DEBUG=True
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.contenttypes','django.contrib.auth','rest_framework','corsheaders','humanitarian']
MIDDLEWARE=['corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware']
ROOT_URLCONF='config.urls'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
USE_TZ=True
CORS_ALLOW_ALL_ORIGINS=True
