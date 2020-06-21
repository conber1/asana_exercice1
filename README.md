Инструкция к выполнению программы:

1) Сделать git clone https://github.com/conber1/asana_exercice1 в определенную папку.

2) Ввести свой ACCESS_TOKEN в файле /offershub_root/settings.py

3) В консоле ввести docker build .

4) В консоле ввесте docker-compose up -d 

5) Узнать номер контейнера командой docker ps -a и войти в контейнер командой docker exec -it id_контейнера /bin/bash 

6) Прописать следующие команды python3 manage.py makemigrations offershub_asana_api, python3 manage.py migrate, python3 manage.py createsuperuser и ввести любой логин и пароль

7) В браузере прописать 0.0.0.0:8000/admin

8)После окончания пользования не забыть прописать docker-compose down 
