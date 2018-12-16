
#items1 = [b"10", b"11", b"12", b"13", b"14"]
#a = random.sample(items1, 2)
#items2 = [b"5", b"4", b"3", b"2", b"1"]
#b = random.sample(items2, 2)
#numbers = arr.array('i')   # creating empty array of integer
#numbers = a + b

#print(numbers) 


#a=bytearray(b'\x00\x00\x00\x01')
#b=bytearray(b'\x00\x00\x00\x02')
#b[0:0] = a

#print(b)

#print(a[3])

import array as arr
import random
import base64



firstbyte=bytearray(b'\x15\x04\xA5')
Firstbyte=random.choice (firstbyte)
q=bytes([Firstbyte])  #0

syncbyte=bytearray(b'\xA5') #1


Lowhi=bytearray(b'\x01\x02')  #3

Transaction_code=bytearray(b'\x75')  #4 ##bunu b'u' olarak okuyor ??????

Hwsn=bytearray(b'\x01\x02\x87\x0b\x1e\x9e\xc9\xde\xb7\x92\n') ##sonuncusu null 11 byte!!! #15

NiBPdatetime=bytearray(b'\x01\x01\x01\x01\x01\x01\x01\x01') #23

spo2alarm_status=bytearray(b'\x00\x01\x02\x03\x04\x08\x0C\x80') 
Spo2alarm_status= random.choice (spo2alarm_status)
w=bytes([Spo2alarm_status])  #24

spo2_cond=bytearray(b'\x10\x11\x12\x20')
Spo2_cond= random.choice (spo2_cond)
e=bytes([Spo2_cond])   #25

spo2=bytearray(b'\x10\x11\x12\x20')
Spo2= random.choice (spo2)
r=bytes([Spo2])   #26

puls=bytearray(b'\x10\x11\x12\x20')
Puls= random.choice (puls)
t=bytes([Puls])   #27

nibp_units=bytearray(b'\x0B\x0C')
Nibp_units=random.choice (nibp_units)
y=bytes([Nibp_units])  #28

nibpmean_status=bytearray(b'\x00\x01\x02\x03\x04\x08')
Nibpmean_status=random.choice (nibpmean_status)
u=bytes([Nibpmean_status])  #29

nibpmean_cond=bytearray(b'\x10\x11\x12\x20')
Nibpmean_cond=random.choice (nibpmean_cond)
ı=bytes([Nibpmean_cond])  #30

nibpmean1=bytearray(b'\x23\x56')
nibpmean2=bytearray(b'\x0B\x0C')
Nibpmean1=random.choice (nibpmean1)
o=bytes([Nibpmean1])  #31
Nibpmean2=random.choice (nibpmean2)
p=bytes([Nibpmean2])  #32

nipb_sysstatus=bytearray(b'\x00\x01\x02\x03\x04\x08')
Nipb_sysstatus=random.choice (nipb_sysstatus)
f=bytes([Nipb_sysstatus])  #33

nipb_syscond=bytearray(b'\x10\x11\x12\x20')
Nipb_syscond=random.choice (nipb_syscond)
g=bytes([Nipb_syscond])   #34

nipb_systolic1=bytearray(b'\x23\x98')
nipb_systolic2=bytearray(b'\x0B\x0C')
Nipb_systolic1=random.choice (nipb_systolic1)
h=bytes([Nipb_systolic1])  #35
Nipb_systolic2=random.choice (nipb_systolic2)
j=bytes([Nipb_systolic2])  #36

nipb_diastatus=bytearray(b'\x00\x01\x02\x03\x04\x08')
Nipb_diastatus=random.choice (nipb_diastatus)
k=bytes([Nipb_diastatus])  #37

nipb_diacond=bytearray(b'\x10\x11\x12\x20')
Nipb_diacond=random.choice (nipb_diacond)
l=bytes([Nipb_diacond])  #38

nipb_diastolic1=bytearray(b'\x23\x98')
nipb_diastolic2=bytearray(b'\x0B\x0C')
Nipb_diastolic1=random.choice (nipb_diastolic1)
v=bytes([Nipb_diastolic1])  #39
Nipb_diastolic2=random.choice (nipb_diastolic2)
b=bytes([Nipb_diastolic2])  #40

checksum=bytearray(b'\x23') #41

numbers = q +syncbyte+ Lowhi+ Transaction_code+ Hwsn+ NiBPdatetime+ w+ e+r+t+ y+ u+ ı+o+ p+ f+g+h+ j+k+l+ v+b+checksum
########liste çevirdim bytearrayi ascii karakterlerden kurtulmak için ama ascii daha iyi olurdu aslında newline 
#mlist=[]
#for i in numbers:
#    b=hex(i).encode()
#   mlist.append(b)          
#z=bytearray(numbers)
#z=bytes([numbers])
#c=[]
#for i in z:   ##making array with hex string
    #integer = i
    #hex_string = '{:02x}'.format(integer)
    #c.append(hex_string)
 

#print(numbers)
#if len(numbers)==40 :
#	print("no data missed")