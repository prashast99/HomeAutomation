from flask import Flask
from flask import Flask, render_template
from flask import render_template, url_for, request
import Adafruit_DHT

import RPi.GPIO as GPIO
import time

pin = 4
sensor = Adafruit_DHT.DHT11

app = Flask(__name__)

led1 = 2
led2 = 3
led3 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)

if (GPIO.setwarnings(False) == False):
    print("Error in rendering")
else:
    time.sleep(2)
    print("Template rendered successfully\n")


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/appliance.html")
def appliance():
    return render_template('appliance.html')

@app.route('/sensor.html')
def index2():
    temperature, humidity = sensor_1()
    return render_template("sensor.html",temperature=temperature, humidity=humidity)

def sensor_1():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity

@app.route('/A')
def led1on():
    data1 = "A"
    GPIO.output(led1, 1)
    return render_template('appliance.html')
    
@app.route('/a')
def led1off():
     data1 = "a"
     GPIO.output(led1, 0)
     return render_template('appliance.html')

@app.route('/B')
def led2on():
    data1 = "B"
    GPIO.output(led2, 1)
    return render_template('appliance.html')
    
@app.route('/b')
def led2off():
     data1 = "b"
     GPIO.output(led2, 0)
     return render_template('appliance.html')

@app.route('/C')
def led3on():
    data1 = "C"
    GPIO.output(led3, 1)
    return render_template('appliance.html')
    
@app.route('/c')
def led3off():
     data1 = "c"
     GPIO.output(led3, 0)
     return render_template('appliance.html')



@app.route("/index.html")
def index3():
    return render_template('index.html')



if __name__ == "__main__":
    print("Starting server")
    for i in range(3):
        print(".")
        time.sleep(1)
    app.run(host='192.168.126.213', port=5010)
