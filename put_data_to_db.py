import pymysql

connection = pymysql.connect(host='10.10.101.161', user='pyuser', password='123456', database='test')

cursor = connection.cursor()

cursor.execute("insert into telsprav values('ramin','kurbanov','m','89659874327')")
connection.commit()

# объеденить файлы put_data  и read_ from и отправить в базу данных из stroki