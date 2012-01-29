# Django settings for snapshot project.
import sys,os

_ = lambda s:s
SITE_NAME='pagina'
PROJECT_PATH=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
APPS_PATH='/'.join([os.path.dirname(PROJECT_PATH),'local_apps'])
#print PROJECT_PATH,APPS_PATH
WWW_ROOT='/'.join([SITE_NAME])
STATIC='/'.join([WWW_ROOT,'static'])
INTERNAL_IPS = ('127.0.0.1',)
ROOT_PATH=os.path.abspath(os.path.dirname( PROJECT_PATH))

sys.path.append(ROOT_PATH)
LOGIN_REDIRECT_URL = WWW_ROOT
LOGIN_URL = WWW_ROOT
AUTH_PROFILE_MODULE = 'local_apps.accounts.Profile'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
     ('canicue', 'canicue@gmail.com'),
     ('canicue', 'canicue@hotmail.com'),
)

MANAGERS = ADMINS
#DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
#DATABASE_NAME = ''             # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '5433'             # Set to empty string for de

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pagina',                      # Or path to database file if using sqlite3.
        'USER': 'canicue',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
EMAIL_HOST = 'localhost'
#EMAIL_HOST_USER = 'dceillan@lam-dan.com.ar'
#EMAIL_HOST_PASSWORD = 'ar5263'
EMAIL_HOST = '200.58.112.185'
EMAIL_HOST_USER = 'canicue@proyectohelado.com.ar'
EMAIL_HOST_PASSWORD = 'canicue'




EMAIL_PORT = 25
EMAIL_USE_TLS = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
LANGUAGES=(('es', 'Spanish'),
 ('pt', 'Portugues'),
 ('en', 'English'),
)
LOCALE_PATHS=('/'.join([PROJECT_PATH,'locale']),)
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l5au-xiiru_ojx$vx3kojvl+zj30_e9b*cp_58cx21ktl14n4k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    #'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
  'dojango.middleware.DojoCollector',
'debug_toolbar.middleware.DebugToolbarMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#'django.middleware.csrf.CsrfResponseMiddleware',

)
SESSION_SAVE_EVERY_REQUEST=False
SESSION_COOKIE_NAME='mec0adfewlamp'

#SESSION_COOKIE_NAME='i44local_buzz_snapshot'

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
'/'.join([ROOT_PATH,'templates'])

)

TEMPLATE_CONTEXT_PROCESSORS=(
        'django.core.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
    'local_apps.tools.context_processors.settings',
    'dojango.context_processors.config',

    )

INSTALLED_APPS = (

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
 #   'django.contrib.restapi',
    'django.contrib.sites',
'local_apps.accounts',

    'chronograph',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup' ,
     'django_extensions',
    'rosetta',
    'dojango',
    'debug_toolbar',
    'mailer',

)
DOJANGO_DOJO_DEBUG=True
DOJANGO_DOJO_PROFILE = 'local_release'
if DOJANGO_DOJO_DEBUG:
    DOJANGO_DOJO_VERSION = 'dev'#buscar la imagen del menu!!!!!!!!!!!!!!
else:
    DOJANGO_DOJO_VERSION = 'prod'

DOJANGO_DOJO_THEME='tema'


DOJANGO_BASE_MEDIA_URL='/'.join([STATIC,'dojo-media'])
DOJANGO_LAYERS='/'.join([STATIC,'dojo-media/release',DOJANGO_DOJO_VERSION,'layers'])#arreglar esto!!!
####DEBUG
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


