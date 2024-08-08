Amélioration de l'architecture modulaire.
=========================================
Fork et clone de l'application.
-------------------------------
Fork du projet pour créer un projet identique sur notre compte GitHub (Clic sur Fork et le nom du projet).
Clone du projet forké sur notre ordinateur local pour isoler notre travail.
Pour récupèrer la copie en local, clic sur Clone, puis copie de l'url du projet, et en console:
``git clone copie de l'url du projet``
La commande ``ls`` affiche le nom du repositrory cloné sur notre poste de travail.

Lancement et test de l'application en local.
--------------------------------------------
En utilisant Git bash:
Tout d'abord nous créeons un environnement virtuel avec la commande:
``python -m venv venv``
Puis on se place dans cet environnement avec la commande:
``source venv/Scripts/activate``
Et nous pouvons alord démarrer l'application avec la commande django:
``python manage.py runserver``
Renvoi de l'erreur: ModuleNotFoundError: No module named 'distutils'

Donc essai mise à jour pip et Django.
``python manage.py runserver``
Nouvelle erreur:
 HINT: Configure the DEFAULT_AUTO_FIELD setting or the OCLettingsSiteConfig.default_auto_field attribute
to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Correction:
Ajout "DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'" dans settings.py
Explications:
Type de champ clé primaire à utiliser par défaut pour les modèles n’ayant pas de champ avec primary_key=True.

La valeur de DEFAULT_AUTO_FIELD sera respectée lors de la création de nouvelles tables intermédiaires
créées automatiquement pour les relations plusieurs-à-plusieurs.
Malheureusement, les clés primaires des tables intermédiaires existantes créées automatiquement
ne peuvent actuellement pas être mises à jour par le système des migrations.
Cela signifie que si vous modifiez la valeur de DEFAULT_AUTO_FIELD,
puis que vous générez des migrations, les clés primaires des modèles liés seront mises à jour,
comme pour les clés étrangères des tables intermédiaires,
mais la clé primaire de ces tables intermédiaires ne seront pas migrées.
Pour corriger cela, vous devez ajouter une opération RunSQL à vos migrations pour effectuer l’étape ALTER TABLE requise.
Vous pouvez obtenir le nom de la table existante au moyen de sqlmigrate, dbshell,
ou avec la propriété remote_field.through._meta.db_table du champ.
Les modèles intermédiaires définis explicitement sont déjà pris en charge par le système des migrations.
La migration automatique des clés primaires des tables intermédiaires existantes créées automatiquement
pourrait être implémentée à une date ultérieure.

Faisons une migration: ``python manage.py migrate``, et relançons:
``python manage.py runserver`` , puis en renseignant ``127.0.0.1:8000`` dans le navigateur le site
semble alors fonctionner, mais nous pouvons optimiser ce projet.

Consulter les ressources, modification des fichiers de migration.
-----------------------------------------------------------------
Nous allons modifier le projet, pour qu'il corresponde à une architecture MVT (Model View Template).
A cet effet, nous allons créer ou modifier 3 dossiers séparés:
- oc_lettings_site
- lettings
- profiles

Création des apps lettings et profiles:
``python manage.py startapp lettings``
``python manage.py startapp profiles``

Création de nouvelles tables.
Ceci implique la modifications des fichiers models.py , views.py de chaque application,
en les réaffectant de leurs classes respectives, le tout suivi d'une migration.
Nous devons également ajouter ces applications dans oc_lettings_site/settings.py
A ce stade la base de donnée est modifiée, et pour remedier au problème du changement de nom des modules,
nous devons créer un utilitaire de transition pour réaffecter ces changements dans la base de donnée:
``tables_update.py``
Cet utilitaire a pour but de migrer les datas de :
oc_lettings_site_address vers lettings_address
oc_lettings_site_letting vers lettings_letting
oc_lettings_site_profile vers profiles_profile
Nous pouvons alors supprimer models.py et modifier views.py de l'application oc_letting_site.

On s'apercoit que le lancement de l'application fonctionne maintenant, mais les liens, ne réagissent plus,
depuis la page d'acceuil.
Il nous faut donc modifier les urls dans chaque application.
Crééons lettings/urls.py et profiles/urls.py et redistribuons les rôles des chemins(Path) depuis oc_lettings_site/urls.

Il nous faut maintenant modifier la base de données pour que les classes nouvellement crées:
- address
- profile
- letting
soient échangées dans cette base:
le fichier précédemment créé va nous permettre de faire cette transition.
Il sera nécéssaire d'ajouter la bib pandas avec pip.
``python tables_updates.py``
En relancant ``python manage.py runserver`` nous pouvons accèder à l'ingégralité du site.

Fin de cette étape particulièrement exigeante.





