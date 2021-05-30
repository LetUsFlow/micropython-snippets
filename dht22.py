import dht
import machine

def get_data():
    d = dht.DHT22(machine.Pin(23))
    d.measure()
    print("Temperature: " + str(d.temperature()))
    print("Humidity: " + str(d.humidity()))

