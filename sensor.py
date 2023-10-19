import serial
import time

ser1 = serial.Serial('/dev/ttyACM0', 2000000)
ser2 = serial.Serial('/dev/ttyACM1', 2000000) #derecha

time.sleep(2)
sensor1 = open("sensor_data1.txt", "w")
sensor2= open("sensor_data2.txt", "w")
init_time = time.time()
final_time = 0

while final_time - init_time < 65:
        try:
            line1 = ser1.readline().decode()
            line2 = ser2.readline().decode()
            print("ser1", line1)
            print("ser2", line2)
        except Exception as e:
            print(e)
        sensor1.write(line1)
        sensor1.flush()
        sensor2.write(line2)
        sensor2.flush()
        final_time = time.time()
ser1.close()
ser2.close()
