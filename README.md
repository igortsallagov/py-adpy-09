# Домашнее задание к лекции 2.4 «Database. Mongo. ORM»

1. Вы реализуете приложение для поиска билетов на концерт. Заполните коллекцию в Монго данными о предстоящих концертах и реализуйте следующие функции:

- `read_data`: импорт данных из csv [файла](https://github.com/netology-code/py-homework-advanced/blob/master/2.4.DB.Mongo.ORM/artists.csv)
- `find_cheapest`: отсортировать билеты из базы по возрастания цены
- `find_by_name`: найти билеты по исполнителю, где имя исполнителя может быть задано не полностью.


## Дополнительное задание

- Реализовать сортировку по дате мероприятия. Для этого вам потребуется строку с датой в csv-файле приводить к объекту datetime (можете считать, что все они текущего года) и сохранять его.

Пример поиска: найти все мероприятия с 1 по 30 июля.
