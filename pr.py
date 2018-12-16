#input b'\xa5' a göre iş yap

import time

import ran

import random

import base64

import sys

import fs as serial 

ser=serial.Serial() ##burda nesneyi yarattım __init__ constructor üne göre parametrede girebilirsin.


class check_error:


    def pocket_data():
  
        
        print("I am sending request for NBP/SpO2 datas")
        
        pocketdata=bytes([0xA5,0x02,0x00,0x50,0xF7])

        ser.write(pocketdata)
        x=ser.read(1)
        ##????????burda cantinue koyarsan ser.read başka bir bytı okur ama serial portta 
        if x==b'\x15':
            print("Negative Acknowledgment.Error occured during data transmission to device.I am sending the datas again... ")
            #w.pocket_data() gerçek portta burayı kullan??????
        elif x==b'\x04':       
            print("Host does not have the capability to respond to the request,it only supports a subset of the protocol") #burayı biraz araştır
            
            sys.exit(["device could not make sense of datas which you just sended.Please check your data"])               
            
        elif x==b'\xa5':
            print("no problem request has sended")
         
                




def send_check75():  #this function request data and check the whether error occured during transmission
    request=check_error
    
    print( request.pocket_data() )    

def func():
    from bitstring import BitArray
    data1=ser.read(1)
    a=data1.hex()

    data2=ser.read(1)
    b=data2.hex()

    c = BitArray(hex=a)

    if data2==b'\x0C':   ##SİGNED OLMASI LAZIM ŞİMDİ SONUÇ NEGATİF OLABİLİR AMA CİHAZA BAĞLANDIĞINDA SIKINTI OLMAZ
        d=c.int/10
    elif data2==b'\x0B' :
        d=c.int

	#c.int converts signed integer 
    print(d,end=' ')

     
    print("Units:",end=' ')
    my_dictSync=dict([("0b", 'mmHg'),("0c", 'kPa(pascal)')]) #???kilopascala çevir
    print(my_dictSync[b]) 

def sync_byte():
    print("Readed bytes: ")
    data=ser.read(1)
    a=data.hex() 
    print("Sync byte:",end=' ')
    my_dictSync=dict([("a5", '0xA5')])
    print(my_dictSync[a])
     ##global r deyipte kullanabilirdik ama nedense buna gerek kalmadı?
     

def lenlo() : ##burda dataları hiç bir işlem yapmadan direk yazdırıyorum şimdilik ???????
    print("Low Order Of Bytes:",end=' ')

    data=ser.read(1) 
    print(data)
    

def lenhi():  ##burda da aynı şekilde
    print("High Order Of Bytes:",end=' ')

    data=ser.read(1) 
    print(data)

def transaction_code():
    print("Transaction code:",end=' ')

    data=ser.read(1) 
    ty=data.hex() 


    my_dictTrans=dict([("75", '0x75')])

    print( my_dictTrans[ty])
    


def hwsn():
    print("Hwsn:",end=' ')
    
    
    data=ser.read(11) 
    
    byteobject= base64.b64encode(data) ##önce stringi decode yaptım byte oldu sonra decodlayıp ıstedıgım stringi bastırdım
	
    print(byteobject)




def NiBPdatetime():
    print("NiBPdatetime:",end=' ')
    
    k=0
    new_data=ser.read(8) #bytes ##6 dan 13 e ikiside dahil
    
    while k<7: #sonraki 8 byte sırasıyla century year felan
        
        
        for i in new_data:
            
            #input_str = q.split(b"\n") ##class artık byte degil list ????bunu split yapmana gerek yok bence zaten tektek byte olarak geliyor
            #c = BitArray(hex=input_str) #hexstringi hexbitstringe çevirdi
        #print(c)
        #print(type(c))   bu bitstring.bitarray
        #print(c.bin)     binary sekilde yazılımı

        #print(c.uint)     #inte çevirdik binaryi şimdi
            nibpdatetime=["century","year","month","day","hour","min","sec","spare"]
            print(nibpdatetime[k],":",i,end=" ")
            k=k+1
    print()

def spo2alarm_status():
    
    data=ser.read(1) 
    a=data.hex() 
    print("SPO2 alarm status:",end=' ')
    my_dictSync=dict([("00", 'No Alarm'),("01", 'Advisory Alarm'),("02", 'Serious Alarm'),("03", 'Life Threatening Alarm'),("04", 'Alarm Active'),("08", 'Alarm Latched'),("0c", 'Alarm Silenced'),("80", 'Alarm Alarm Off')])
    print(my_dictSync[a])     

def spo2_cond():
    
    data=ser.read(1) 
    a=data.hex() 
    print("SPO2 Cond.:",end=' ')
    my_dictSync=dict([("10", 'Condition overrange "+++"'),("11", 'Condition underrange "---"'),("12", 'Technical condition "***"'),("20", 'Parameter Blank " "')])
    print(my_dictSync[a])

def spo2():
    from bitstring import BitArray

    data=ser.read(1) 
    a=data.hex()
    c = BitArray(hex=a) #hexstringi hexbitstringe çevirdi
       

    ##c.uint    #inte çevirdik binaryi şimdi yani base10

    print("SPO2:",c.uint,"%(in percent)")


def puls():
    from bitstring import BitArray

    data=ser.read(1)
    
    
    a=data.hex()
    c = BitArray(hex=a) #hexstringi hexbitstringe çevirdi
       

    ##c.uint    #inte çevirdik binaryi şimdi yani base10

    print("PULS:",c.uint,"beats per minute")   

def nibp_units():
    data=ser.read(1)
    
    a=data.hex() 
    print("NiBP Units:",end=' ')
    my_dictSync=dict([("0b", 'mmHg'),("0c", 'NiBP degeri/10 kPa(kilopascal)')])
    print(my_dictSync[a])
        
def nibpmean_status ():
    data=ser.read(1)
    a=data.hex() 
    print("NiBP Mean Status:",end=' ')
    my_dictSync=dict([("00", 'No Alarm'),("01", 'Advisory Alarm'),("02", 'Serious Alarm'),("03", 'Life Threatening Alarm'),("04", 'Alarm Active'),("08", 'Alarm Latched'),("80", 'Alarm Alarm Off')])
    print(my_dictSync[a]) 

def nibpmean_cond():
    data=ser.read(1)
    a=data.hex() 
    print("NiBP Mean Cond.:",end=' ')
    my_dictSync=dict([("10", 'Condition overrange "+++"'),("11", 'Condition underrange "---"'),("12", 'Technical condition "***"'),("20", 'Parameter Blank " "')])
    print(my_dictSync[a])   

def nibpmean():
    print("Nibp Mean:",end="")
    func()
    
def nipb_sysstatus():
    data=ser.read(1)
    a=data.hex() 
    print("NiBP Sys. Status:",end=' ')
    my_dictSync=dict([("00", 'No Alarm'),("01", 'Advisory Alarm'),("02", 'Serious Alarm'),("03", 'Life Threatening Alarm'),("04", 'Alarm Active'),("08", 'Alarm Latched'),("80", 'Alarm Alarm Off')])
    print(my_dictSync[a]) 

def nipb_syscond():
    data=ser.read(1)
    a=data.hex() 
    print("NiBP Sys. Cond:",end=' ')
    my_dictSync=dict([("10", 'Condition overrange "+++"'),("11", 'Condition underrange "---"'),("12", 'Technical condition "***"'),("20", 'Parameter Blank " "')])
    print(my_dictSync[a])        

def nipb_systolic():
    print("Nipb Siastolic:",end="")
    func()

def nipb_diastatus():
    data=ser.read(1)
    a=data.hex() 
    print("NiBP Dia. Status:",end=' ')
    my_dictSync=dict([("00", 'No Alarm'),("01", 'Advisory Alarm'),("02", 'Serious Alarm'),("03", 'Life Threatening Alarm'),("04", 'Alarm Active'),("08", 'Alarm Latched'),("80", 'Alarm Alarm Off')])
    print(my_dictSync[a])      
	
def nipb_diacond():
    data=ser.read(1)
    a=data.hex() 
    print("NiBP Dia. Cond.:",end=' ')
    my_dictSync=dict([("10", 'Condition overrange "+++"'),("11", 'Condition underrange "---"'),("12", 'Technical condition "***"'),("20", 'Parameter Blank " "')])
    print(my_dictSync[a])    

def nipb_diastolic(): 
    print("Nipb Diastolic:",end="")
    func()

def checksum():
    print("Checksum:",end=' ')
    print(ser.read(1))

def menu():
    print("welcome :) ")
    print()
    print("to request the software ID and Server Status string press 2")
    print()
    print("to request the NBP/SpO2 data press 1. (This is for Telemetry interface only)")
    print()


class Cmd75:    
    pass

def send75():
    
    cmd75 = Cmd75()
    cmd75.Send_check75 = send_check75()
    return Cmd75



def read75():           #?????bu ser i alttaki fonksiyonların içinede yazmalı mıyım ??
    cmd75 = Cmd75()

    cmd75.SyncByte = sync_byte() 
    cmd75.Lenlo = lenlo()	#???? gelen dataya bak muhtemelen checksum calculation da işe yarayacak
    cmd75.Lenhi = lenhi()   #?????
    cmd75.TransactionCode = transaction_code()
    cmd75.Hwsn = hwsn()  #???? heterogeneus wireless sensor networks 
    cmd75.NiBPdate_time = NiBPdatetime()
    cmd75.SPO2Alarm_status = spo2alarm_status()
    cmd75.SPO2_Cond = spo2_cond()
    cmd75.SPO2 = spo2()
    cmd75.PULS = puls()
    cmd75.NiBP_Units = nibp_units()   ###??? dataya bak belki de  bunu ayrıca yazdırmamalısın
    cmd75.NiBPMean_Status = nibpmean_status ()
    cmd75.NiBP_MeanCond = nibpmean_cond()
    cmd75.NiBP_Mean = nibpmean()
    cmd75.NiBP_SysStatus = nipb_sysstatus()
    cmd75.NiBP_SysCond = nipb_syscond()
    cmd75.NiBP_Systolic  = nipb_systolic()
    cmd75.NiBP_DiaStatus = nipb_diastatus()
    cmd75.NiBP_DiaCond = nipb_diacond()
    cmd75.NiBP_Diastolic = nipb_diastolic()
    cmd75.Checksum = checksum()

    return Cmd75

if __name__ == '__main__':
        
        ser.open() 
        print()    
        menu()	
        while True:  

            n=int(input("press a key"))
            
            if n==1 :
                send75()
                read75()
	

            print("to exit press 0 or to go back to menu press 3 " )
            n=int(input("press a key"))

            if n==3:
                menu()
                continue

            elif n==0 :
                print("bye bye " )		
                break		

