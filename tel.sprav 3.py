import pymysql



while True:
    connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
    cursor = connection.cursor()
    username = input('Ведите имя абонента:')
    cursor.execute(f'SELECT name , phone from telsprav WHERE name = "{username}"')
    connection.close()
    data = cursor.fetchall()
    print(data)
    #print(data[0][0],data[0][1])
    print(len(data))
    if len(data)> 0:
        name = data[0][0]
        phone = data[0][1]
        print(f'Телефон абонента {username} - {[phone]}')
    else:
        print(f'Телефон абонента {username} - не найден ')


