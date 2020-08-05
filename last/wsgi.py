"""
WSGI config for last project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
python_home='/path/to/your/venv'
activate_this=python_home+'/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'last.settings')

application = get_wsgi_application()
