import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from apps.posts.tasks import reset_post_up_votes

    sender.add_periodic_task(crontab(hour=0, minute=0),
                             reset_post_up_votes.s())
