### Что это ?

  Приложение для розыгрыша бесплатного [курса](https://otus.ru/lessons/7/) на дне открытых дверей.

  Модули приложения работают внутри контейнеров и запускаются с помощью docker-compose


### Использование
```
$ git clone https://github.com/express42/gilmore.git
$ cd gilmore
$ docker-compose up
```
  * В браузере открыть страницу с адресом localhost:5000
  * Выбрать файл в формате csv ("Выберите список")
  * Нажать "Загрузить"
  * Нажать "Разыграть"
  * Ждать окончания таймера
  * Порадоваться или огорчиться

### Состав
  * [Docker](https://www.docker.com/) и [Docker-compose](https://docs.docker.com/compose/)
  * Docker контейнер с приложением
    * Веб-приложение на языке Python (фреймворк  [Flask](http://flask.pocoo.org/]), Jinja-шаблоны)
    * Веб-страница - JavaScript, ajax, html, css
  * Контейнер с базой данных mongodb

### Алгоритм
  Выбор победителя выполняется по следующему алгоритму:
  * Загружается список участников
  * Выбирается случайный отрезок времени (внутри заданного промежутка)
  * В ходе выбранного отрезка времени происходит перебор случайных чисел в пределах числа участников
  * Скорость перебора выигрышного числа падает с течением времени в зависимости от всего времени работы алгоритмаы
  * По истечении таймера выбирается 1 победитель
