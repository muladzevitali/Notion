# Python test assessment by DevelopsToday

## Links:

* Heroku app: [URL](https://sleepy-brook-01727.herokuapp.com/api/v1/posts)
* Github: [URL](https://github.com/muladzevitali/notion.git)
* Postman collection: [URL](https://documenter.getpostman.com/view/4089546/UVBzoVpU)

# Steps for building the project

* Firstly you are required to install Docker, Docker compose on you machine
* For starting the service run

```bash
docker-compose up --build
```

## Usage:

Current application includes two entities: [posts](app/apps/posts/models.py) and [comments](app/apps/posts/models.py).
For the post we have the following operations: __create post__, __retrieve/get the post__, __list all the posts__, __
update the post__,
__delete the post__ and __upvote the post__.

For the comment we have same operations except comment can't be up voted.

Url and methods for each operation can be found on the postman collection above.

As required every day at 00:00 AM scheduled job is running and making number of up votes zero. I have implemented this
with the celery beat scheduler.

Also, every used technology can be found in [file](app/requirements.txt)

