import os
BASE_DIR = os.path.dirname(__file__)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "..", 'db.sqlite3'),
    }
}
DEBUG = True
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_mathjax',
    'django.contrib.messages'
)
TEMPLATES = [    
        {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   
            'DIRS': [os.path.join(BASE_DIR,'..', 'templates')], # For those who wants to have a custom place for templates in their Django apps/projects.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
MIDDLEWARE =    ['django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware']

ROOT_URLCONF = 'zeke.urls'
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "..", "static"),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "..", "templates"),
)
MATHJAX_ENABLED=True