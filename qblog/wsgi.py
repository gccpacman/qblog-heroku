"""
WSGI config for qblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qblog.settings")
# from dj_static import Cling
# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

# application = get_wsgi_application()
# application = Cling(get_wsgi_application())
# application = DjangoWhiteNoise(application)


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
