import time

import generate_array

import random






r=generate_array.numbers

class Serial: 

    def __init__( self, port='COM1', baudrate = 19200, timeout=1,
                  bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                  rtscts = 0):

        self._isOpen  = True

    def open( self ):  
        
        self._isOpen = True 
        print("The port has opened")         
  
    
    def read(self,x):
        
        global r
 
        s=r[0:x]
        r=r[x:]
  
        return s

    def write(self,x):
        print("port has this bytes:")
        i=0
        while i<len(x) :
            a=hex(x[i])
            print(a.encode(),end=" ") 
            i=i+1
        print()