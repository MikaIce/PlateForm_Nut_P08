import os
import sys
import newrelic.agent

from django.core.wsgi import get_wsgi_application

# Chemin absolu du répertoire 'platform'
platform_path = '/home/mbenoit/platform'

# Ajoutez le chemin du répertoire 'platform' à la variable sys.path
sys.path.append(platform_path)

# Définissez le répertoire 'core' comme le chemin du module wsgi
wsgi_path = os.path.join(platform_path, 'core')

# Assurez-vous que le chemin du module 'core.wsgi' est correct
wsgi_module = 'core.wsgi'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purbeurre.settings')

# Utilisez le chemin complet du module wsgi
application = get_wsgi_application()

newrelic.agent.initialize('/home/mbenoit/platform/newrelic.ini')
