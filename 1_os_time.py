import os

print('Jestem w',os.getcwd())    #pokaż, gdzie jesteś
os.chdir('C:\\Users\\musiakam\\Desktop')   #zmień ścieżkę
#os.chdir(r'C:\Users\musiakam\Desktop')    #r - raw string, robi to samo, co powyższa linia
print('Jestem w',os.getcwd())

os.mkdir('new_folder')