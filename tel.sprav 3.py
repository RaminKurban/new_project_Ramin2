# capitalize - выравнивание букв, большая или маленькая
import pymysql
import  datetime

phone_cache = {}

while True:

    username = input('Ведите имя абонента:').capitalize()
    start_time = datetime.datetime.now()

    phone = phone_cache.get(username, None)
    if  phone != None:
        print(f'Телефон абонента {username} - {[phone]}')
        print('из словаря')

    else:
        connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test',
                                     port=33306)
        cursor = connection.cursor()
        cursor.execute(f'SELECT name , phone from telsprav WHERE name = "{username}"')
        connection.close()
        data = cursor.fetchall()
    if len(data) > 0:
        name = data[0][0]
        phone = data[0][1]
        print(f'Телефон абонента {username} - {[phone]}')
        print('из БЗ')
        phone_cache[username] = phone
    else:
        print(f'Телефон абонента {username} - не найден ')
end_time = datetime.datetime.now()
work_time = email - start_time
print(work_time)