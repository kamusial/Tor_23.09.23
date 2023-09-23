import time
import datetime

now = datetime.datetime.now()
moja_nazwa = now.strftime('report%H%M%S.txt')

for i in range(10):
    now = datetime.datetime.now()
    moja_nazwa = now.strftime('report%H%M%S.txt')
    print('moja nazwa to', moja_nazwa)
    time.sleep(2)


