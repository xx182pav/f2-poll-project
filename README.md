# f2-poll-project


# Для развертывания пректа в Docker.

 - скопировать репозиторий
 - docker-compose up -d --build запустить контейнеры  
 - docker-compose exec web python manage.py migrate --noinput  проведения миграции


 - Сайт работает по адресу 127.0.0.1:8000 

Для деплоя на heroku необходимо:
1) В терминале зайти в директорию проекта:
2) Выполнить следующие команды:
   - git init
   - git add .
   - git commit -m "initial commit"
   - heroku login
   - heroku create
   - heroku addons:create heroku-postgresql:hobby-dev
   - heroku config:set DISABLE_COLLECTSTATIC=1
   - git push heroku master
   - heroku run python manage.py  migrate
   - heroku open

-- Проект находится на https://f2-poll-project.herokuapp.com/
