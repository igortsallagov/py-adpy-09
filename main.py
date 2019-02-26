import csv
import re
from pymongo import MongoClient
from datetime import datetime


def read_data(csv_file, database):
    with open(csv_file, encoding='utf8') as csvfile:
        rows_list = list()
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = dict(row)
            row['Цена'] = int(row['Цена'])
            row['Дата'] += '.2019'
            row['Дата'] = datetime.strptime(row['Дата'], '%d.%m.%Y')
            rows_list.append(row)
        database.insert_many(rows_list)


def find_cheapest(database):
    sorted_list = list(database.find().sort('Цена', 1))
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


def find_by_name(name, database):
    name = re.escape(name)
    regex = re.compile(name)
    sorted_list = list(database.find({'Исполнитель': regex}).sort('Цена', 1))
    print(f'Найдено мероприятий: {len(sorted_list)}')
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


def find_by_date_range(start_date, end_date, database):
    start_date = datetime.strptime(start_date, '%d.%m.%Y')
    end_date = datetime.strptime(end_date, '%d.%m.%Y')
    sorted_list = list(database.find({'Дата': {'$gt': start_date, '$lt': end_date}}))
    print(f'Найдено мероприятий: {len(sorted_list)}')
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


if __name__ == '__main__':
    client = MongoClient()
    db = client.tickets_db
    ticket_db = db.ticket
    read_data('artists.csv', ticket_db)
    find_cheapest(ticket_db)
    find_by_name('t', ticket_db)
    find_by_date_range('01.01.2019', '30.03.2019', ticket_db)
