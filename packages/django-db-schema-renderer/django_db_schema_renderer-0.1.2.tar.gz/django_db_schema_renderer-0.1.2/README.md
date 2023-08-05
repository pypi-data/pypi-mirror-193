# Django-db-schema-renderer

## Overview

This is a django app to render db schema (ER diagram), of selected models or apps inside django admin panel

## Requirements

- Python 3.7+
- Django 3.1+
- django-extensions 3+
- pygraphviz 1.7+

For successful install of pygraphviz you need to have on your host graphviz installed. you can find official docs [here](https://graphviz.org/download/)
On apple silicon this can be achieved by running command:

```bash
brew install graphviz
pip3 install \
    --global-option=build_ext \
    --global-option="-I$(brew --prefix graphviz)/include/" \
    --global-option="-L$(brew --prefix graphviz)/lib/" \
    pygraphviz
```

## Installation

1. Install using `pip`...

   pip install django-db-schema-renderer

2. Add `django_db_schema_renderer` to your `INSTALLED_APPS` setting, before `django.contrib.admin`(make sure you have `django-extensions` also added)

   ```python
   INSTALLED_APPS = [
       'django_db_schema_renderer',
       'django.contrib.admin',
       ...
       'django-extensions'

   ]
   ```

3. Edit the `{project_dir}/urls.py` module in your project:

   ```python
   from django_db_schema_renderer.urls import schema_urls

   urlpatterns = [
   ...
    path("db-schema/", include((schema_urls, "db-schema"))),
   ...
   ]

   ```
