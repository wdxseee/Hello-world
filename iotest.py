# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:44:34 2017

@author: hfvy

digital 测试
"""

import pifacedigitalio as dio
from time import sleep

dio.init()

def r():
    while True:
        print dio.digital_read(0)
        #print dio.digital_read(1)
        #print dio.digital_read(2)
        #print dio.digital_read(3)
        #print dio.digital_read(4)
        #print dio.digital_read(5)
        #print dio.digital_read(6)
        #print dio.digital_read(7)
        sleep(1)
def w():
    dio.digital_write(0,1)
    #dio.digital_write(1,1)
    #dio.digital_write(2,1)
    #dio.digital_write(3,1)
    #dio.digital_write(4,1)
    #dio.digital_write(5,1)
    #dio.digital_write(6,1)
    #dio.digital_write(7,1)

def q():
    dio.init()    