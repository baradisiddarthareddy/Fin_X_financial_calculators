"""
WSGI config for financial_calculators project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
# Replace 'yourusername' with your actual PythonAnywhere username
path = '/home/245121733067/Fin-X/render/financial_calculators'
if path not in sys.path:
    sys.path.append(path)

# Set the environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'financial_calculators.settings'

# Initialize the Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

