#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, math, serial, requests

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
pulse = 0
start_timer = time.time() 
r_cm=42
sensor1 = 11 # GPIO17
sensor2 = 13 # GPIO27

def init_GPIO():   
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(sensor1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
      GPIO.setup(sensor2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def calculate_speed(channel):
            global start_timer,pulse,elapse,rpm,dist_km,dist_meas,km_per_sec,km_per_hour, payload

            elapse = time.time() - start_timer
            start_timer = time.time() 
            rpm = 1/elapse * 60
            circ_cm = (2*math.pi)*r_cm           # calculate wheel circumference in CM
            dist_km = circ_cm/100000             # convert cm to km
            km_per_sec = dist_km / elapse        # calculate KM/sec
            km_per_hour = km_per_sec * 3600      # calculate KM/h
            
            if channel == 11:
                              datos = [channel,rpm,dist_km,km_per_hour]
                              print(datos)
            
            if channel == 13:
                              datos = [channel,rpm,dist_km,km_per_hour]
                              print(datos)

def switchoff(channel):
      print("off:"+channel)

def init_interrupt():
      GPIO.add_event_detect(sensor1, GPIO.RISING, callback=calculate_speed)
      GPIO.add_event_detect(sensor2, GPIO.RISING, callback=calculate_speed)

try:
      print "Start!"
      init_GPIO()
      init_interrupt()
      while True: time.sleep(1e9)
finally:
    GPIO.cleanup()
