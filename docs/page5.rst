Documentation de l'application.
===============================
SPHINX:
-------
Récupération sphinx avec pip install (voir requirements.txt)
Création du dossier docs, puis depuis ce dossier lancer:
sphinx-quickstart
Congiguration avec config.py
Changement de thème avec 'sphinx_rtd_theme'
Actuellement il y a conflit avec docutils et 'sphinx_rtd_theme':
=> retour à la version docutils==0.20.1 (au lieu de 0.21.2) et CicleCi donne un retour 'success'.

Complèter index.rst et eventuellement ajouter d'autres pages.rst (ReStructuredText files).
Valider avec la commande: make html ou (git bash:`` ./make.bat html``)
Nous pouvons maintenant accèder à ou aux pages crées à partic du dossier docs/_builds/html/index.html

Revenir dans le dossier racine du projet, lancer la commande:
``sphinx-apidoc -o docs .`` pour pouvoir afficher l'ensemble des modules et fonctions depuis ``.`` les modules
du dossier racine.
A partir de _build/html/index.html nous pouvons alors avoir accès à la documentation du projet avec le navigateur.

La phase suivante est d'enregistrer le projet sur readthedocs:
Il s'agit simplement de référencer le projet github sur readthedocs et de valider la compilation.
Ensuite, Readthedocs propose le lien qui va permettre de visualiser le projet dans le navigateur.

La mise à jour s'effectuera automatiquement à chaque commit avec git.