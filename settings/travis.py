from purbeurre.settings import *

# Paramètres spécifiques à l'environnement Travis CI
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci_test',  # Nom de la base de données pour Travis
        'USER': 'postgres',  # Utilisateur par défaut de Travis
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Autres paramètres spécifiques à Travis CI, si nécessaire
# Par exemple, vous pouvez modifier le niveau de journalisation ou désactiver certains plugins

