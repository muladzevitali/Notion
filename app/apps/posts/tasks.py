from config.celery import app
from .models import Post


@app.task(bind=False)
def reset_post_up_votes():
    Post.objects.update(num_upvote=0)
