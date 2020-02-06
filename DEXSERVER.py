import serial
import time
FCODE=""

Ardno = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2)
Ardno.write('sta'.encode())

data = Ardno.readline() #the last bit gets rid of the new-line chars
print(data)
