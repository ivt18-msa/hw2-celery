# Обработка длительных заданий

Напишите веб-сервис для архивации данных:

* Пользователь может получить список существующих заархивированных файлов.
* Пользователь может скачивать ранее заархивированные файлы.
* Пользователь может загрузить новый файл.
* При добавлении нового файла веб-сервис должен сжать его с помощью архиватора.
* Пользователь должен иметь возможность указать один из 3 архиваторов.
* При сжатии веб-сервис должен продолжать свою обычную работу.
* Веб-сервис должен быть написан на Flask
* Обработка архивации должна выполняться с помощью фонового задания Celery

## Ссылки

* [Документация Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Документация Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* [Модуль subprocess](https://docs.python.org/3/library/subprocess.html)
* [Пример работы с Celery](https://blog.miguelgrinberg.com/post/using-celery-with-flask)
* [Сборки Redis для Windows](https://github.com/microsoftarchive/redis/releases)
