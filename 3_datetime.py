import datetime

now = datetime.datetime.now()
print(now)
print(type(now))

_time = now.strftime('Data to: %d-%m-%y\nGodzina to: %H - %M - %S')
print(_time)

moja_nazwa = now.strftime('Plik_%H%M%S.txt')
print('moja nazwa to',moja_nazwa)
