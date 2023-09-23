import os

os.system('  cmd /c "ipconfig /all > dane.txt  "   ')

path = 'dane.txt'
mode = 'r'
with open(path, mode, encoding="utf8", errors="ignore") as moj_plik:
    content = moj_plik.readlines()

nr_linii = 0
for i in range(len(content)):
    if '(Preferred)' in content[i]:
        content[i] = content[i].split(':')
        nr_linii = i

print(content[nr_linii][1][1:-13])

