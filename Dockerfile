FROM python:3.9-slim

ENV DJANGO_SETTINGS_MODULE="config.settings"
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential curl libpq-dev --no-install-recommends
RUN useradd --create-home notion
RUN chown notion:notion -R  /tmp /app

RUN mkdir /var/log/celery -p
RUN mkdir /var/run/celery -p
RUN chown -R notion:notion /var/log/celery/
RUN chown -R notion:notion /var/run/celery/

USER notion

COPY --chown=notion:notion app/requirements.txt /app

ENV PYTHONUNBUFFERED="${PYTHONUNBUFFERED}" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/notion/.local/bin" \
    USER="notion"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY --chown=notion:notion app /app
COPY --chown=notion:notion .env /app/.env
COPY --chown=notion:notion app-entrypoint.sh /


RUN chmod u+x /app-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]