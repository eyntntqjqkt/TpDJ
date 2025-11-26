from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY="demo"
DEBUG=True
ALLOWED_HOSTS=[]
INSTALLED_APPS=[
 'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
 'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
 'students',
]
MIDDLEWARE=[
 'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',
]
ROOT_URLCONF="demoDjango.urls"
TEMPLATES=[{
 'BACKEND':'django.template.backends.django.DjangoTemplates',
 'DIRS':[], 'APP_DIRS':True,
 'OPTIONS':{'context_processors':['django.template.context_processors.debug',
  'django.template.context_processors.request','django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages']},
}]
WSGI_APPLICATION="demoDjango.wsgi.application"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_7y0q_user',
        'USER': 'dj',
        'PASSWORD': 'e5KXOZRFHFPzVFwEpRroG3uZdAd7l19m',
        'HOST': 'dpg-d4jekrer433s739bapl0-a',
        'PORT': '5432',
    }
}