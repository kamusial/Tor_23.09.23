path = 'rozliczenie.csv'
mode = 'r'
with open(path, mode) as moj_plik:
    content = moj_plik.readlines()

print(content)

for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3])
print(content[3][2])   #pierwszy index - wiersz, drugi index - kolumna
print(content[0][2][3:-2])    #3ci indeks, znaki stringa

#string.replace('\n','')

print('\n\n')
#przykład replace
slowo = 'mama.tata'
slowo = slowo.replace('a', 'A', 2)
print(slowo)

#przyklad split
slowo = 'mama.tata'
slowo = slowo.split('.')
print(slowo)