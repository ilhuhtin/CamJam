# CamJam Edukit 2 - Sensors
# Worksheet 2 - LEDs and Buzzer

# Import Python libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the three GPIO pins for Output

GPIO.setup(18, GPIO.OUT) # Red 
GPIO.setup(24, GPIO.OUT) # Blue
#GPIO.setup(22, GPIO.OUT) # Buzzer

print("Lights and sound on")

# Red On
GPIO.output(18, GPIO.HIGH)

# Pause
time.sleep(1)

# Blue On
GPIO.output(24, GPIO.HIGH)

# Pause
time.sleep(1)

#Buzzer On
#GPIO.output(22, GPIO.HIGH)

# Pause
time.sleep(1)

print("Lights and sound off")

# Red Off
GPIO.output(18, GPIO.LOW)

# Pause
time.sleep(1)

# Blue Off
GPIO.output(24, GPIO.LOW)

# Buzzer Off
#GPIO.output(22, GPIO.LOW)

GPIO.cleanup()
