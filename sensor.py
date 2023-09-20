import serial
import time
#Configure the serial port. Replace 'COM3' with the appropriate port name on your system.
ser = serial.Serial('/dev/ttyACM0', 9600)

# Create a text file to store the sensor data
with open('sensor_data.txt', 'w') as file:
    final_time=0
    init_time = time.time()
    while final_time - init_time < 5:
        # Read a line of data from the Arduino via serial
        line = ser.readline().decode('utf-8')
        
        # Write the data to the text file
        file.write(line)
        file.flush()  # Ensure data is written immediately
        
        # Print the data to the console (optional)
        print(line, end='')
        final_time = time.time()

# Close the serial port when done
ser.close()





