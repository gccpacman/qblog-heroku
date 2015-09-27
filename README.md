This project was built to demonstrate Django especially new features of Django 1.7. It builds a blog application. More details can be found at http://arunrocks.com

Perview: https://young-earth-1871.herokuapp.com/

Read this:
[Getting Started with Django on Heroku | Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-django)
[Configuring Django Apps for Heroku | Heroku Dev Center](https://devcenter.heroku.com/articles/django-app-configuration)
[Building a Blog with Django 1.7 in 16 mins - YouTube](https://www.youtube.com/watch?v=7rgph8en0Jc)
[Deploy | Django Girls 學習指南](https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/deploy.html)

Something Try But not use yet:
[etianen/django-herokuapp](https://github.com/etianen/django-herokuapp)

## Steps

1. Create a *Procfile*, and insert code below:

	web: gunicorn qblog.wsgi --log-file -

2. Add these to requirement.txt, and install them by pip later:

```
	dj-database-url==0.3.0
	dj-static==0.0.6
	gunicorn==19.1.1
	psycopg2==2.5.1
	static==0.4
	wsgiref==0.1.2
```

3. Replace your database settings with Heroku’s Postgres database :

``` python
    import dj_database_url
    DATABASES = {
        'default':  dj_database_url.config()
    }
```
    
4. Allow HTTPS *SECURE_PROXY_SSL_HEADER*, add code below in settings.py:

``` python
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

5. change content in wsgi.py to something like this:

    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())

6. Deploy to Heroku, push code to heroku repo:

    $ heroku create
    $ git push heroku master

7. Check and Visit your site:

    $ heroku ps:scale web=1
    $ heroku ps   # you should check at least one instance is running
    $ heroku open   # this will open default browser for you

8. If it is not working , you can debug on you local machine: 

    	$ gunicorn qblog.wsgi --log-file -

    	$ heroku local   # (does not working yet.)

9. You also should check the remote Heroku logs:

    $ heroku logs


10. other things to be research:

Whitenoise can organize you static file properly, put these in settings.py 

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
