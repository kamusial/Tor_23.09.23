import os
import time

print('Jestem w',os.getcwd())    #pokaż, gdzie jesteś
os.chdir('C:\\Users\\vdi-student\\Desktop')   #zmień ścieżkę
#os.chdir(r'C:\Users\vdi-student\Desktop')    #r - raw string, robi to samo, co powyższa linia
print('Jestem w',os.getcwd())

os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', 'newer_folder')
time.sleep(2)
os.rmdir('newer_folder')
time.sleep(2)
print('zrobione')

os.system('  cmd /c "cd C:\\Users\\vdi-student\\Desktop   &&   echo Kamil >> dane.txt  "   ')
#wejdź na pulpit i wpisz 'Kamil' do pliku dane.txt

#os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop && dir /s new.txt >> result.txt"')