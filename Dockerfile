FROM python:3.11.3-slim-buster
LABEL maintainer="andriyvvoznyuk@gmail.com"

ENV DockerHOME=/app
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    gettext \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install "gunicorn==20.0.4"

# Install the project requirements.
COPY requirements.txt .

RUN pip install  -r requirements.txt



# Copy the source code of the project into the container.
COPY . .

# Collect static files.
#RUN python manage.py makemigrations --settings=core.settings.production
#RUN python manage.py migrate --settings=core.settings.production
#RUN python manage.py collectstatic --settings=core.settings.production --no-input --clear
#RUN python manage.py update_index --settings=core.settings.production
#RUN gunicorn core.wsgi:application -b :8082  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
#CMD set -xe; python manage.py migrate --noinput; gunicorn core.wsgi:application
