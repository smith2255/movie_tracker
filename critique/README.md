$ represents running a command in terminal

1. Download and install Docker-Engine, and Docker-Compose
2. $ docker-compose build
3. $ docker-compose up db
4. Now that the db service is up, open another terminal and
execute $ docker exec -t -i critique_db_1 /bin/bash
5. $ psql
6. $ create database movie_tracker;
7. $ \q - close this terminal
8. hit 'ctrl-c' in the terminal where the service database is running.
9. $ 'docker-compose up' - this will bring up django with the
database
10. open a new terminal, run command 'docker exec -t -i critique_django_1 /bin/bash'
11. $ ./manage.py migrate
12. $ ./manage loaddata fixture_users.json
12. $ ./manage loaddata fixture_reviews.json