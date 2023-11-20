#Регулярные данные ( выборка)
# re - регулярные выражения, библеотека
import re
stroka = 'Privet, menya zovut Kirill, mne 38 let, moy telefon 89110271345, a pochta kmmorozov@gmail.com'

result = re.match(r'Pri', stroka)

print(result)