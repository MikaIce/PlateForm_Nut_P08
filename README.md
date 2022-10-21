Créez une plateforme pour amateurs de Nutella

Description du projet :

La startup Pur Beurre, avec laquelle vous avez déjà travaillé, souhaite développer une plateforme web à destination de ses clients. 
Ce site permettra à quiconque de trouver un substitut sain à un aliment considéré comme 
"Trop gras, trop sucré, trop salé" (même si nous savons tous que le gras c’est la vie).

Fonctionnalités :

Affichage du champ de recherche dès la page d’accueil
Interface responsive
Authentification de l’utilisateur : création de compte en entrant un mail et un mot de passe, 
sans possibilité de changer son mot de passe pour le moment.

Installation :

1 Installez les dépendances du fichier requirements.txt.

2 Créer une base de données avec postgreSQL nommée 'purbeurre'.
Vous pouvez configurer les options qui vous sont personnelles dans le fichier settings.py dans la partie DATABASE = { }.

3 Dans le fichier settings.py, configurez l'option 'ALLOWED_HOSTS' de la manière suivante: 
ALLOWED_HOSTS = ['*'] ou  ALLOWED_HOSTS = ['name_app.herokuapp.com', '0.0.0.0', '127.0.0.1']

4 En local
Lancez le fichier manage.py en console de cette manière: python manage.py runserver

5 En ligne
Cette application est aussi utilisable en ligne.

Elle est hébergée sur Heroku ici --> https://purbeurnut.herokuapp.com/

Fabriqué avec :

Python 10.7
Django 
Postresql
Bootstrap 4

Auteurs :

BENOIT Michael 
