from machine import UART
from time import sleep


def get_data():
	uart = UART(1, 9600)

	uart.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
	sleep(0.05)
	res = uart.read(9)
	
	if len(res) == 9:
	    checksum = 0xff & (~(res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]) + 1)
	    if res[8] == checksum:
		print("CO2: " + str((res[2] << 8) | res[3]))
            else:
                print("Error reading CO2-Level")

