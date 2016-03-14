"""
Standalone test runner for Guidelines plugin
"""
import os
import sys

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE='guidelines.tests.dummy_options_module',
                   ROOT_URLCONF='guidelines.urls',
                   STATIC_URL='/assets/',
                   STATIC_ROOT='static',
                   STATICFILES_FINDERS=(
                       'django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       'compressor.finders.CompressorFinder',),
                   COMPRESS_ROOT='/tmp/',
                   MIDDLEWARE_CLASSES=(
                       'django.middleware.common.CommonMiddleware',
                       'django.contrib.sessions.middleware.SessionMiddleware',
                       'opal.middleware.AngularCSRFRename',
                       'django.middleware.csrf.CsrfViewMiddleware',
                       'django.contrib.auth.middleware.AuthenticationMiddleware',
                       'django.contrib.messages.middleware.MessageMiddleware',
                       'opal.middleware.DjangoReversionWorkaround',
                       'reversion.middleware.RevisionMiddleware',
                       'axes.middleware.FailedLoginMiddleware',
                   ),
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'django.contrib.staticfiles',
                                   'compressor',
                                   'opal',
                                   'opal.tests',
                                   'guidelines',),
                   MIGRATION_MODULES={
                       'opal': 'opal.nomigrations'
                   }
)

from opal.core import application
class Application(application.OpalApplication):
    pass


import django
django.setup()

# from guidelines.tests import dummy_options_module


from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['guidelines', ])
if failures:
    sys.exit(failures)
