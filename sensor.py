import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

init_time = time.time()
final_time = 0
with open("sensor_data.txt", "w") as sensor_file:
    while final_time - init_time < 30:
        try:
            line = ser.readline().decode()
            print(line)
        except Exception as e:
            print(e)
        sensor_file.write(line)
        sensor_file.flush()
        final_time = time.time()
ser.close()
