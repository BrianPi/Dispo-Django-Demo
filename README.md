# Dispo Django Demo

A demo API that allows users to create and like posts and follow other users, completed on request as a demonstration for Dispo.

## Features
1. `POST` endpoints for user, post, and user following. `PUT` endpoint for toggling post likes.
   
1. `GET /users/top`, which returns a list of users with one or more posts sorted by number of posts authored descending, and `GET /users/feed/<user_id>` that returns a list of posts created by the user or anyone they follow with number of likes received in reverse chronological order.

1. A custom post serializer, so that post output has the following structure:
   ```
   {
     "id": <post id>,
     "body": <post body>,
     "author": <post author's username>,
     "likes": <post like count>
   }
   ```

1. A custom user class, derived from `AbstractUser`, to allow for follow relations while still using the basic Django user authentication. It's worth noting that this class invites potential database migration pain if it needs to be modified.
   
## Setup
* After installing [Poetry](https://python-poetry.org), use `poetry install` to  set up your environment.
    * Alternatively, you can manage the `django` and `djangorestframework` dependencies yourself.
* Initialize SQLite database
    * Poetry: `poetry run python manage.py migrate`
* Run the server (default port 8000)
    * Poetry: `poetry run python manage.py runserver`

## LICENSE

DO NOT USE. THIS REPO IS FOR EVALUATION AND TESTING PURPOSES ONLY.
