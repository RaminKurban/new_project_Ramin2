# range - диопозон (чисел)
a = range(1, 100)
users = ('kirill', 'ivan', 'pavel', 'petr')
print(type(a))
print(type(users))
print(a)
for element in a:
    print(element * 2)

for user in users:
    print(f'уважаемый {user},добро пожаловать')
# f - форматированная строка