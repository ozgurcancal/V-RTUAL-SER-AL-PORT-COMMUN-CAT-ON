import time

import ran

import random






r=ran.numbers

class Serial: ##burayı serial fonksiyonlarını kullanabilmek için yazdım

    def __init__( self, port='COM1', baudrate = 19200, timeout=1,
                  bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                  rtscts = 0):

        self._isOpen  = True

    def open( self ):  #???
        
        self._isOpen = True 
        print("The port has opened")         
    #def write(X): 
        #print("Device got:" ,X )
        #data=X
    
    def read(self,x):
        
        global r
        #if bytes([data[len(data)-1]])=bytearray(b'\x57') :  ###bytes([ ]) direk ascii ye çevirir.
         #   print("received bytes:",end="")
        s=r[0:x]
        r=r[x:]
        #print("readed byte: ",end="")
        #print(s)
        return s

    def write(self,x):
        print("port has this bytes:")
        i=0
        while i<len(x) :
            a=hex(x[i])
            print(a.encode(),end=" ") 
            i=i+1
        print()