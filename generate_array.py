import array as arr
import random
import base64

firstbyte=bytearray(b'\x15\x04\xA5')
Firstbyte=random.choice (firstbyte)
q=bytes([Firstbyte])  

syncbyte=bytearray(b'\xA5') 

Lowhi=bytearray(b'\x01\x02')  

Transaction_code=bytearray(b'\x75')  

Hwsn=bytearray(b'\x01\x02\x87\x0b\x1e\x9e\xc9\xde\xb7\x92\n') 

NiBPdatetime=bytearray(b'\x01\x01\x01\x01\x01\x01\x01\x01') 

spo2alarm_status=bytearray(b'\x00\x01\x02\x03\x04\x08\x0C\x80') 
Spo2alarm_status= random.choice (spo2alarm_status)
w=bytes([Spo2alarm_status])  

spo2_cond=bytearray(b'\x10\x11\x12\x20')
Spo2_cond= random.choice (spo2_cond)
e=bytes([Spo2_cond])   

spo2=bytearray(b'\x10\x11\x12\x20')
Spo2= random.choice (spo2)
r=bytes([Spo2])   

puls=bytearray(b'\x10\x11\x12\x20')
Puls= random.choice (puls)
t=bytes([Puls])   

nibp_units=bytearray(b'\x0B\x0C')
Nibp_units=random.choice (nibp_units)
y=bytes([Nibp_units])  

nibpmean_status=bytearray(b'\x00\x01\x02\x03\x04\x08')
Nibpmean_status=random.choice (nibpmean_status)
u=bytes([Nibpmean_status])  

nibpmean_cond=bytearray(b'\x10\x11\x12\x20')
Nibpmean_cond=random.choice (nibpmean_cond)
ı=bytes([Nibpmean_cond])  

nibpmean1=bytearray(b'\x23\x56')
nibpmean2=bytearray(b'\x0B\x0C')
Nibpmean1=random.choice (nibpmean1)
o=bytes([Nibpmean1])  
Nibpmean2=random.choice (nibpmean2)
p=bytes([Nibpmean2])  

nipb_sysstatus=bytearray(b'\x00\x01\x02\x03\x04\x08')
Nipb_sysstatus=random.choice (nipb_sysstatus)
f=bytes([Nipb_sysstatus])  

nipb_syscond=bytearray(b'\x10\x11\x12\x20')
Nipb_syscond=random.choice (nipb_syscond)
g=bytes([Nipb_syscond])   

nipb_systolic1=bytearray(b'\x23\x98')
nipb_systolic2=bytearray(b'\x0B\x0C')
Nipb_systolic1=random.choice (nipb_systolic1)
h=bytes([Nipb_systolic1])  
Nipb_systolic2=random.choice (nipb_systolic2)
j=bytes([Nipb_systolic2])  

nipb_diastatus=bytearray(b'\x00\x01\x02\x03\x04\x08')
Nipb_diastatus=random.choice (nipb_diastatus)
k=bytes([Nipb_diastatus])  

nipb_diacond=bytearray(b'\x10\x11\x12\x20')
Nipb_diacond=random.choice (nipb_diacond)
l=bytes([Nipb_diacond])  

nipb_diastolic1=bytearray(b'\x23\x98')
nipb_diastolic2=bytearray(b'\x0B\x0C')
Nipb_diastolic1=random.choice (nipb_diastolic1)
v=bytes([Nipb_diastolic1])  
Nipb_diastolic2=random.choice (nipb_diastolic2)
b=bytes([Nipb_diastolic2])  

checksum=bytearray(b'\x23') 

numbers = q +syncbyte+ Lowhi+ Transaction_code+ Hwsn+ NiBPdatetime+ w+ e+r+t+ y+ u+ ı+o+ p+ f+g+h+ j+k+l+ v+b+checksum
