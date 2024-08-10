Surveillance de l'application et des erreurs avec Sentry.
=========================================================
En pré-requis nous devons installer sentry-sdk avec pip:
``pip install --upgrade sentry-sdk``
Sentry est ensuite initialisé dans oc_lettings_site/settings.py :
Init Sentry:
------------
sentry_sdk.init(dsn,
                integrations=[DjangoIntegration()],
                max_breadcrumbs=50,
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
                debug=False,
                )
dsn est enregistré dans un fichier .env non commité.

Nous avons la possibilité de vérifier le fonctionnement de Sentry:
# urls.py
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]


Définition des niveaux de logs pour les différentes parties de l'application.
Repèrer les points critiques, et y insérer des logs (ex: try except.)
Logs avec msg erreurs.
Vérification des logs avec introduction d'erreurs.