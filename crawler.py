import urllib.request
from random import choice
from string import digits
from threading import Thread
a = 1

def function(i):

    while a==1:
        id = ''.join(choice(digits) for i in range(8))
        url = "http://194.87.218.32/stat.php?id="+id
        print (url)
        res = urllib.request.urlopen(url)
        html = res.read().decode('utf-8', 'ignore')
        if "Run" in html:
            print ("Поток %i YAAAAAAAAAAAAAAAAY" %i)
            with open('good.txt' , 'a') as f:
                f.write(url+"\n")
        else:
            print("Поток %i DOWP" %i)
    


for i in range(10000):
    th = Thread(target=function, args=(i, ))
    th.start()