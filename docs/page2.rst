Résolution des problemes du projet.
===================================
Après toutes ces modifications, note application est maintenant fonctionnelle.

Admin:
------
Nous devons maintenant redistribuer oc_lettings_site/admin.py dans les modules profiles/admin.py et lettings/admin.py,
et supprimer le dossier oc_lettings_site/admin.py
Dorénavant nous avons accès à l'administration en ligne.

Correction du linting avec flake8:
----------------------------------
Revue du code et nettoyage lignes inutiles.
``flake8`` renvoie tous les fichier à formater conformément à PEP8.

Gestion des erreurs 404 et 500:
-------------------------------
Création de pages personnalisées (error404.html, error500.html) pour les erreurs sus mentionnées,
dans le dossier templates à la racine. Ces erreurs sont appellées par différentes fonctions dans les views de chaques
applications.

Création de docstrings sur les modules les classes et les fonctions:
--------------------------------------------------------------------
Les docstrings doivent expliquer la fonctionnalité, les paramètres, la valeur de retour et
tout autre détail important du code.

Gestion de la couverture de tests (>80%):
-----------------------------------------
J'ai utilisé pytest-cov, retournant un résultat de 71%, avec la commande ``pytest --cov=.``

Regroupement des tests par applications, en créant un dossier tests dans lettings et profiles.





