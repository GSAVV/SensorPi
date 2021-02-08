from pigpio_dht import DHT22

# IMPORTANT: run "sudo pigpiod" to run the daemon for the sensor

gpio = 4    # BCM Numbering
sensor = DHT22(gpio)

result = sensor.sample(samples=5)
print(result)
