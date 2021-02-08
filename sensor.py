from pigpio_dht import DHT22
from time import sleep
import urllib.request

def init():
    global sensor, pin, sensorname, db_ip, php_script

    pin = 4                     # BCM numbering of data PIN
    sensor = DHT22(pin)         # initialize sensor object
    sensorname = 'sensor2'      # important for the database
    db_ip = '192.168.178.50'   # for GET request
    php_script = 'add_data.php' # script name on the DB server

    return

def main():
    global sensor, pin, sensorname, db_ip, php_script

    # Get raw data
    try:
        reading = sensor.sample(samples=3)
    except TimeoutError:
        reading = {'temp_c': '-1', 'humidity': '-1'}

    # Convert to strings
    t = '{:.1f}'.format(reading['temp_c'])
    h = '{:.1f}'.format(reading['humidity']) 

    # Build GET request string
    urlS = 'http://' + db_ip + '/' + php_script + '?temp=' + t + '&hum=' + h + '&name=' + sensorname
    #print(urlS)

    # Send data
    urllib.request.urlopen(urlS)

    return

init()
while True:
    main()
    sleep(300)
