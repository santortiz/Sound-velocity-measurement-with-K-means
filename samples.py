import serial
import time
#Configure the serial port. Replace 'COM3' with the appropriate port name on your system.
ser = serial.Serial('/dev/ttyACM0', 16000000)


lines_per_sample = []
n_sample=0
while n_sample < 20:
    init_time = time.time()
    final_time = 0
    print("muestra tal: ", n_sample)
    with open(f"samples/sample_{n_sample}.txt", "w") as sample_file:
        n_lines= 0
        while final_time - init_time < 3:
            try:
                line = ser.readline().decode()
                n_lines += 1
            except Exception as e:
                print(e)
                continue
            sample_file.write(line)
            sample_file.flush()
            final_time = time.time()
    lines_per_sample.append(n_lines)
    n_sample += 1

with open("samples/lines_per_sample2.txt", "w") as lines_file:
    lines_file.write(str(lines_per_sample))
    lines_file.flush()
ser.close()





