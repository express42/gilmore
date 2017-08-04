### Что это ?

  Небольшое демонстрационное приложение для выбора случаного участника состоящее из веб-сервера на языке Python и базы данных mongodb
  Модули приложения работают внутри контейнеров и запускаются с помощью docker-compose

  Для выбор участника выполняется по следующему алгоритму:
  * Выбирается случайный отрезок времени (внутри заданного промежутка)
  * В ходе выбранного отрезка времени происходит перебор случайных чисел в пределах числа количества участников
  * Скорость перебора выигрышного числа падает с течением времени в зависимости от всего времени работы алгоритмаы

### Использование
```
docker-compose up
```
* В браузере открыть страницу с адресом localhost:5000
* Выбрать и загрузить файл в формате csv
* Нажать "Разыграть"
* Ждать окончания таймера
