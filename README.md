# SensorPi
A Raspberry Pi Zero W temperature and humidity sensor which logs to Postgres via GET requests

## Hardware
* Raspberry Pi Zero W
* SEN-DHT22 Sensor (Joy-IT, integrated resistor, 1-wire protocol)

## Software
* Raspberry OS (Buster, 01-11-2021)
* Python 3.7
* pigpiod
* a DB server which accepts the GET requests! (**not included here**, implement e.g. with this [tutorial](http://educ8s.tv/raspberry-pi-online-weather-log/))

## Preparing the board
* "burn" the iso file onto an SD card
* add an empty file called `ssh` (without extension) into the boot partition
* add the configuration file `wpa_supplicant.conf` for the WIFI connectivity to the boot partition (needs Linux line endings! Use Notepad++ to ensure this!):
```
country=DE 
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev 
update_config=1 
network={
     ssid="WLAN SSID"
     scan_ssid=1
     psk="WLAN PASSWORT"
     key_mgmt=WPA-PSK
}
```
* put the SD card into the RasPi and connect the DHT sensor as shown to pins 3v3, GPIO4, GND ![Pinout](info/GPIO.png)
* boot the Pi and SSH in
* then run `passwd` for pi user and `sudo passwd` for su user
* then run `sudo raspi-config` to set locale, hostname, enable Pin IO and I2C. (GUI can be turned off)
* reboot
* give static IP adress via options in the router (leave the Pi on DHCP mode)
* update the system and go drink some coffee 
```
sudo apt-get update
sudo apt-get upgrade
```

## Preparing the program
First, we get everything from github.com
```
mkdir sensorpi
cd sensorpi
git clone https://github.com/GSAVV/SensorPi.git
sudo chmod +x startup.sh
```

Then, we install the dependencies
```
sudo pip3 install pigpio-dht
```

After that, we set the connection details of the PG server inside the `sensorpi.py` script

Finally, we add the following line to the `/etc/rc.local` file
```
python3 /home/pi/sensorpi/startup.sh &
```
