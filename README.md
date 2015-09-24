This project was built to demonstrate Django especially new features of Django 1.7. It builds a blog application. More details can be found at http://arunrocks.com

Perview: https://young-earth-1871.herokuapp.com/

Read this:
[Getting Started with Django on Heroku | Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-django)
[Configuring Django Apps for Heroku | Heroku Dev Center](https://devcenter.heroku.com/articles/django-app-configuration)
[Building a Blog with Django 1.7 in 16 mins - YouTube](https://www.youtube.com/watch?v=7rgph8en0Jc)

Something Try But not use yet:
[etianen/django-herokuapp](https://github.com/etianen/django-herokuapp)


Test on your host: 

    gunicorn qblog.wsgi --log-file -

    OR

    heroku local(not working yet)

View Heroku logs:

    heroku logs

Checkout Heroku server status:

    heroku ps


Whitenoise can organize you static file properly, put these in settings.py 

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
