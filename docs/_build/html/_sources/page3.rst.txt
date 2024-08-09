Surveillance de l'application et des erreurs avec Sentry.
=========================================================
Sentry est initialisé dans oc_lettings_site/settings.py :
# ============= Init Sentry ============= #
sentry_sdk.init(dsn,
                integrations=[DjangoIntegration()],
                max_breadcrumbs=50,
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
                debug=False,
                )
dsn est enregistré dans un fichier .env non commité.


Définition des niveaux de logs pour les différentes parties de l'application.
Repèrer les points critiques, et y insérer des logs (ex: try except.)
Logs avec msg erreurs.
Vérification des logs avec introduction d'erreurs.