# moduleD6_homework
Cайт на Django 

## Описание
В данном репозитории вы можете скачать простой сайт-библиотеку на Django, здесь вы можете вести книги имеющиеся в вашей библиотеке, список авторов, издательств, друзей (которые взяли почитать у вас книгу)

## Инструкция
* Скачайте архив сайта по ссылке https://github.com/AndruRus/moduleD5_homework/archive/main.zip. 
*Распакуйте архив
* Создайте виртуальное окружение для проекта
* Для того чтобы быстро установить все требуемые библиотеки python в новом окружении достаточно выполнить команду "pip install -r requirements.txt"
* Dыполнить команду "python manage.py createsuperuser" и ввести данные
* Запуск по команде "python manage.py runserver" из дирректория my_site в котором находиться "manage.py".  
* По ссылке http://127.0.0.1:8000/ находится страница с книгами и авторами их написавшими.
* По ссылке http://127.0.0.1:8000/friends-list/ находится страница с книгами и друзьями которые их взяли. 
* По ссылке http://127.0.0.1:8000/publishinghouses находится страница с издательствами.
* По ссылке http://127.0.0.1:8000/admin/ находится страница администрирования проекта, где Вы можете добавлять, удалять, редактировать пунткы: Авторы, Книги, Друзья(читатели), Издательства.
* Добавлять изображения книг возможно только из панели Администратора.

## D5_10_Heroku

Действия в Git
$ git init
$ git add .
$ git commit -m "initial commit"
$ heroku create
$ heroku config:set DISABLE_COLLECTSTATIC=1 -- Для того чтобы небыло ошибки запрещаем на время установки обращение к статическим файлам

Правим модуль в Heroku
Resources => добавляем Heroku Postgres
Settings => Reveal Config Vars добавляем SECRET_KEY и его значение

$ git add .
$ git commit -m "about to deploy"
$ git push heroku master
После получения положительного результата о установке
$ heroku config:set DISABLE_COLLECTSTATIC=0 -- Подключаем статические файлы после установки приложения
$ heroku run python manage.py migrate
$ heroku run python manage.py loaddata data.xml
$ heroku run python manage.py createsuperuser


https://floating-mesa-85238.herokuapp.com


     
    