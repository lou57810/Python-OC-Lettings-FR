Mise en place du déploiement avec Docker, et le pipleline Cicd:
===============================================================
Plusieurs étapes seront nécéssaires pour le déploiement de notre application.

Docker:
------
Création d'un container et d'une image pour notre application.
Tout d'abord, installer Docker en local, et s'enregistrer sur Docker Hub.
Nous devons également créér un Dockerfile à la racine de l'application:
Ce fichier décrit l'ensemble des étapes à réaliser pour pouvoir lancer notre application.
Chaque instruction que nous allons donner dans notre Dockerfile va créer une nouvelle layer,
correspondant à chaque étape de la construction de l'image.
Comme exemple, à la base:
``# base image
FROM python:3.12``

Gunicorn:
---------
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server Web for UNIX.
Gunicorn joue le rôle d'un serveur web(adapté au langage Python), comme par exemple d'autres comme
Apache ou Nginx, mais en version légère.
Nous avons besoin de renseigner sa fonction dans le Dockerfile:
``CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]``

Revenons en à Docker:
---------------------
Créeons également un fichier .dockerignore dans lequel les étapes inutiles peuvent être ignorées.

Enfin,
- création de l'image avec la commande suivante:
    ``docker build -t nom_application . ``
    L'argument -t permet de donner un nom à votre image Docker.
    Cela permet de retrouver plus facilement l' image par la suite.
    Le . est le répertoire où se trouve le Dockerfile ; dans notre cas, à la racine de notre projet.
- lancement du container:
    ``docker run -d -p 8000:8000 nom_application`` (-p = port 8000:8000 pour Django)
    Le premier port est interne et le deuxième externe.
- Nous pouvons accèder à notre application en lancant dans le navigateur: http://127.0.0.1:8000


Docker Hub
----------
Pour l'instant, notre application est joignable en local, mais nous voulons la rendre publique.
Pour rendre cette image publique,  allons la publier sur Docker Hub,
en lançant les commandes suivantes:
``docker tag ocr-docker-build:latest YOUR_USERNAME/nom_application:latest`` (Crée un lien entre l'image créée et
  l'image à envoyer.)
Puis:
``docker push YOUR_USERNAME/nom_application:latest``
Voilà, l'image figure sur une 'Registry' sur Docker Hub.

Render:
-------
Render est une plateforme populaire pour le déploiement de pages web et d’applications.
Nous avons Docker pour le stockage de notre application, Gunicorn comme Server Web, mais,
pour le moment, il nous manque un hébergeur.
C'est ici que Render rentre en fonction pour la diffusion de notre application sur la toile.
Mais nous devons renseigner quelques variables pour l'utiliser.
Dans la rubrique Settings:
- Name: Python-OC-Lettings-FR
- Région: Frankfurt (EU Central)
Dans Build & Deploy:
- Repository: https://github.com/lou57810/Python-OC-Lettings-FR
-Branch: 'main' (Dans notre cas)
- Deploy hook: (Render propose de la générer ou de la changer automatiquement.)
Dans la rubrique Environnement:
- SECRET_KEY: La variable que nous avons défini dans le fichier à la racine: .env

CircleCi:
---------
CircleCi est l'outil manquant au développement de notre application:
CircleCi permet de tester chaque commit réalisé avec git, et remonter les informations de défaillance ou de succès.
Pour celà il nous renseigner quelque indications et en particulier les variables d'environnement:
- DEBUG = False
- DEPLOY_HOOK = (valeur générée et figurant dans Render/Deployhook)
- DOCKER_HUB_PASSWORD = personal_password_hub (Le mien ou le vôtre)
- DOCKER_HUB_USER_ID = personal_user_id (Le mien ou le vôtre)
- SECRET_KEY = celui défini dans racine/.env
- dsn = celui défini dans racine/.env

Création d'un fichier local pour les variables d'environnement.
Configuration Django en mode production.
Si vous utilisez Render comme solution de déploiement, veillez à désactiver le déploiement automatique à chaque commit.