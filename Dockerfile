# base image
FROM python:3.12

# Maintenance dockerfile:
# MAINTAINER lou57810 <lou57810@foo.com>	deprecated
ENV PYTHONBUFFERED 1
# Eviter les fichiers .pyc dans les containers --> ralentissements
ENV PYTHONDONTWRITEBYTECODE 1

# Installer les dépendances système nécessaires
# RUN apt-get update && \
    # apt-get install -y build-essential libffi-dev libpq-dev libssl-dev && \
    # apt-get clean

RUN mkdir /app

# copy all content to work directory /app
COPY . /app
WORKDIR /app

# install dependencies in requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
RUN python manage.py collectstatic --noinput
 
ADD oc-lettings-site.sqlite3 /app

# volume:
# 	- static: /static

ENV SENTRY_DSN="https://7a43cfd6cd09fa8a09e97279d8f37881@o4506869492940800.ingest.us.sentry.io/4507153243963392"
ENV SENTRY_ENVIRONMENT=production


# specify the port number the container should expose
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
