Mise en place Cicd
==================
Surveillance de l'application et des erreurs avec Sentry.
---------------------------------------------------------
Configuration symétrique de Sentry.
Définition des niveaux de logs pour les différentes parties de l'application.
Repèrer les points critiques, et y insérer des logs (ex: try except.)
Logs avec msg erreurs.
Vérification des logs avec introduction d'erreurs.

Mise en place du déploiement avec Docker, Cicd et Render.
---------------------------------------------------------
Lancement auto de CI après chaque commit.
Création d'une image docker tournant en local.
Push de l'image sur Docker Hub.
Déploiement avec image publique.
Création d'un fichier local pour les variables d'environnement.
Configuration Django en mode production.
Si vous utilisez Render comme solution de déploiement, veillez à désactiver le déploiement automatique à chaque commit.

Documentation de l'application.
-------------------------------
SPHINX:
Récupération sphinx avec pip install (voir requirements.txt)
Création du dossier docs, puis dans ce dossier lancer:
sphinx-quickstart
Congiguration avec config.py
Complèter index.rst et eventuellement ajouter d'autres pages.rst (ReStructuredText files).
Valider avec la commande: make html ou (git bash: ./make.bat html)
Revenir dans le dossier racine du projet et lancer la commande:
sphinx-apidoc -o docs .

A partir de _build/html/index.html nous pouvons alors avoir accès à la documentation du projet avec le navigateur.

Mise à jour auto à chaque modif.
