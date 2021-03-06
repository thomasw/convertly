# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# List of all installed authentication backends
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

# List of template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'context_processors.default',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	#'django.contrib.admin',
	'django_extensions',
	#'south',
	'compress',
	'converter',
	'gunicorn',
	'sentry.client',
)

# Login configuration
#LOGIN_URL = '/login/'
#LOGOUT_URL = '/logout/'
#LOGIN_REDIRECT_URL = '/'

# Profile Configuration
# AUTH_PROFILE_MODULE = "accounts.Profile"

# djanog-compress settings.
COMPRESS_CSS = {
	'main': {
		'source_filenames': (
			'css/convertly.css',
		),
		'output_filename': 'css/convertly.r?.css',
    },
}

COMPRESS_JS = {
	'main': {
		'source_filenames': (
			'js/googleAnalytics.js',
			'js/form.js',
			'js/convertly.js',
		),
		'output_filename': 'js/convertly.r?.js',
	},
}

# Import local settings.
try:
    from local_settings import *
except ImportError:
    pass