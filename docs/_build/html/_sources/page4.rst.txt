Mise en place du déploiement avec Docker, et le pipleline Cicd:
===============================================================

Docker:
-------
Création d'un container et d'une image pour notre application.
Tout d'abord, installer Docker en local, et s'enregistrer sur Docker Hub.
Nous devons également créér un Dockerfile à la racine de l'application:
Ce fichier décrit l'ensemble des étapes à réaliser pour pouvoir lancer notre application.
Chaque instruction que nous allons donner dans notre Dockerfile va créer une nouvelle layer,
correspondant à chaque étape de la construction de l'image.
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



Mise en place du déploiement avec Docker, Cicd et Render.
---------------------------------------------------------
Tout d'abord, nous devons rendre notre image publique, et pour celà, nous allons la publier sur Docker Hub,
en lançant les commandes suivantes:
``docker tag ocr-docker-build:latest YOUR_USERNAME/nom_application:latest`` (Crée un lien entre l'image créée et
  l'image à envoyer.)
Puis:
``docker push YOUR_USERNAME/nom_application:latest``
Voilà, l'image figure sur une 'Registry' sur Docker Hub.

Lancement auto de CI après chaque commit.
Création d'une image docker tournant en local.
Push de l'image sur Docker Hub.
Déploiement avec image publique.
Création d'un fichier local pour les variables d'environnement.
Configuration Django en mode production.
Si vous utilisez Render comme solution de déploiement, veillez à désactiver le déploiement automatique à chaque commit.