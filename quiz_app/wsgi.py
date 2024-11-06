import os
import sys

# Add the project directory to the sys.path
path = '/home/yourusername/my_django_project'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_django_project.settings'

# Activate the virtual environment
activate_this = '/home/yourusername/myvenv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django’s WSGI application handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
