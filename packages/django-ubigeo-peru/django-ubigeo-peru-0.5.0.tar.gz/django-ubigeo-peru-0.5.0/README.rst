Django Ubigeo Peru
===================

django-ubigeo-peru, is an app that will allow you to easily implement the ubiquites of INEI (Perú) in your django app.


Config
------

For Django >= 4.x use django-ubigeo-peru>=0.5.0

In your **settings.py**

.. code-block:: python

  INSTALLED_APPS = (
      .....
      'ubigeos',
  )

Run

::

  python manage.py migrate
  python manage.py loaddata ubigeos.json


In your **urls.py**

For Django <= 1.11.x

.. code-block:: python

  urlpatterns = patterns('',
      .....
      (r'^ubigeos/', include('ubigeos.urls')),
  )


For Django 2.x and above

.. code-block:: python

  urlpatterns = patterns('',
      ....
      path('ubigeos/', include('ubigeos.urls')),
  )


License
--------

BSD
