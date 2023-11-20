#Регулярные выражения ( выборка)
# re - регулярные выражения, библеотека
# match - поиск в строке, с начало , по буквам
# search - поиск в самой строке
# split - разбиение (разделитель)
# findall - поиск  слова в строке ( колличество )
# \d - вывод всех цифр
# \d+ - на одно или более вхождений
# \d{7,11} - от семи до 11 знаков
# \b\d\d\d\d\d\d\d\b - начало или конец слова , 7 цифр
# | - или
# \w+ - одна или более букв
# [] - это список, где перечисляются элементы ( помидоры , огурцы и тд)
# {} - это словарь, где содержаться пары, ключ и значения ( помидоры 200рублей, помидоры 300 рублей)
import re
import  requests


stroka = 'Privet, menya zovut Kirill, mne 38 let, moy telefon 89110271345, a pochta kmmorozov@gmail.com, moy index 12345678'

result = re.match(r'Privet, menya zovut Kirill', stroka)

print(result)
print(result.group(0))
print(result.start())
print(result.end())

#############


result = re.search(r'telefon',stroka)
print(result)
############

result = re.split(r'moy',stroka)
print(result)
#############

result = re.findall(r'telefon',stroka)
print(result)
#################

phones = re.findall(r'\d',stroka)
print(phones)

phones = re.findall(r'\d+',stroka)
print(phones)

phones = re.findall(r'\d{7,11}',stroka)
print(phones)

phones = re.findall(r'\b\d\d\d\d\d\d\d\b|\b\d\d\d\d\d\d\d\d\d\d\d\b',stroka)
print(phones)
#######################
result = requests.get('http://www.ipap.ru')
text = result.text
emails = re.findall(r'\w+@\w+.\w\w+',text)
print(emails)
#################

