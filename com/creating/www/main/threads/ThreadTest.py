# -*- coding: utf8 -*-
'''
Created on 2018��12��28��

@author: developorName
'''
import threading
def runx(n):
    while True:
        print("hello")
    
if __name__ == '__main__':
    t1 = threading.Thread(target=runx, args=(2,))
    t2 = threading.Thread(target=runx, args=(3,))
    t3 = threading.Thread(target=runx, args=(4,))
    #t1.start()
    #t2.start()
    #t3.start()
    runx(1)
    pass