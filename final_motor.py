import RPi.GPIO as GPIO
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from firebase import firebase
import schedule 

GPIO.setmode(GPIO.BCM)

firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)


lcd = Adafruit_CharLCD(rs=26,en=19,
		d4=13, d5=6,d6=5,d7=11,
		cols=16,lines=2)
lcd.clear()

ControlPin = [4,17,21,22]

ControlPin2 = [22,21,17,4]

photores = 23

#pilltime = firebase.get('/Cureent Schedule/Darel Diaz/Hours1',None)

#int_pilltime = int(pilltime)

pilltime = 1

message = ("Pill wasnt Taken")
message2 = ("Pill was Taken")

def rc_time(photores):
	count=0
	GPIO.setup(photores,GPIO.OUT)
	GPIO.output(photores,GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(photores,GPIO.IN)

	while (GPIO.input(photores) == GPIO.LOW):
		count += 1
	return count

def capstone():


	message_motor1 = firebase.get('/Current Schedule/Darel Diaz/Name1',None)
	message2_motor1 = firebase.get('/Current Schedule/Darel Diaz/Dose1',None)

	for pin in ControlPin:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,0)

	seq= [ [1,0,0,0],
	       [1,1,0,0],
	       [0,1,0,0],
	       [0,1,1,0],
	       [0,0,1,0],
	       [0,0,1,1],
	       [0,0,0,1],
	       [1,0,0,1] ]

	for i in range (512):
		for halfstep in range(8):
			for pin in range(4):
				GPIO.output(ControlPin[pin], seq[halfstep][pin])

			time.sleep(0.001)


	lcd.message("Pill Name: " + message_motor1 + "\n" + "Take: " +  message2_motor1 + " pill")

	if rc_time(photores) > 200000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		firebase.post('/test',message)

		for pin2 in ControlPin2:
			GPIO.setup(pin2,GPIO.OUT)
			GPIO.output(pin2,0)

		seq2 = [ [1,0,0,0],
			 [1,1,0,0],
	 	 	 [0,1,0,0],
	 	 	 [0,1,1,0],
	 	 	 [0,0,1,0],
	 	 	 [0,0,1,1],
	 	 	 [0,0,0,1],
	 	 	 [1,0,0,1]  ]

		for i in range (512):
			for halfstep in range(8):
				for pin2 in range(4):
					GPIO.output(ControlPin2[pin2], seq2[halfstep][pin2])
				time.sleep(0.001)
		lcd.clear()
	else:
		firebase.post('/test',message2)

		for pin2 in ControlPin2:
			GPIO.setup(pin2,GPIO.OUT)
			GPIO.output(pin2,0)

		seq2 = [ [1,0,0,0],
			 [1,1,0,0],
	 	 	 [0,1,0,0],
	 	 	 [0,1,1,0],
	 	 	 [0,0,1,0],
	 	 	 [0,0,1,1],
	 	 	 [0,0,0,1],
	 	 	 [1,0,0,1]  ]

		for i in range (512):
			for halfstep in range(8):
				for pin2 in range(4):
					GPIO.output(ControlPin2[pin2], seq2[halfstep][pin2])
				time.sleep(0.001)
		lcd.clear()

schedule.every(pilltime).minutes.do(capstone)

while True:

	schedule.run_pending()
	time.sleep(1)


GPIO.cleanup()
