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
Mise à jour auto à chaque modif.
