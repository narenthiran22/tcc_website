# tcc_website/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tcc_website.settings')

application = get_wsgi_application()

# Vercel needs the variable to be named 'app'
app = application