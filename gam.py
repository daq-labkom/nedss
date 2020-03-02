import requests
import math
import random
import time

while True:
    GAM1= str(random.randrange(5,20))
    GAM2= str(random.randrange(2,10))
    GAM3= str(random.randrange(30,40))
    GAM4= str(random.randrange(14, 19))
    GAM5= str(random.randrange(0,35))
    GAM6= str(random.randrange(10,30))
    r= requests.get("http://localhost/nedss/simulasi.php?GAM1="+GAM1+"&GAM2="+GAM2+"&GAM3="+GAM3+"&GAM4="+GAM4+"&GAM5="+GAM5+"&GAM6="+GAM6)
    print(r.text)
    time.sleep(1)