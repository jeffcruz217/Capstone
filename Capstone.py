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

#ControlPin = [4,17,27,22]

#ControlPin2 = [22,27,17,4]

#ControlPin = [12,16,20,21]

#ControlPin2 = [21,20,16,12]

ControlPin = [18,24,25,8]

ControlPin2 = [8,25,24,18]

photores = 23

buzzer = 10

please = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

pilltime2= int(please)

message = ("Pill wasnt Taken")
message2 = ("Pill was Taken")

#def quantity():
#	quant = firebase.get('/Current Schedule/Darel Diaz/Qty1', None)
#	quantity = int(quant)

#	return quantity
def buzzer(buzzer):
	GPIO.setup(buzzer,GPIO.OUT)
	GPIO.output(buzzer,GPIO.HIGH)
	GPIO.output(buzzer,GPIO.HIGH)
	GPIO.output(buzzer,GPIO.HIGH)

def Update_Capstone():

	pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

	pilltime = int(pillhour)

	return pilltime

def rc_time(photores):
	count=0
	GPIO.setup(photores,GPIO.OUT)
	GPIO.output(photores,GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(photores,GPIO.IN)

	while (GPIO.input(photores) == GPIO.LOW):
		count += 1
	return count

def motor1_up():
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
	buzzer()

def moror1_down():

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
	 	 	 [1,0,0,1] ]

	for i in range (512):
		for halfstep in range(8):
			for pin2 in range(4):
				GPIO.output(ControlPin2[pin2], seq2[halfstep][pin2])
			time.sleep(0.001)
		

def capstone():


	message_motor1 = firebase.get('/Current Schedule/Darel Diaz/Name1',None)
	message2_motor1 = firebase.get('/Current Schedule/Darel Diaz/Dose1',None)

	#Dose = int(message2_motor1)

#/////////////////////////////////1
	
	motor1_up()


	lcd.message("Pill Name: " + message_motor1 + "\n" + "Take: " +  message2_motor1 + " pill")

	if rc_time(photores) > 200000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		firebase.post('/test',message)

		#//////////////////////////////////2
		moror1_down()

		lcd.clear()
	

	else:
		#qty = quantity()
		#newqty = qty - Dose

		firebase.post('/test',message2)
		#firebase.post('/Current Schedule/Darel Diaz/Qty1', newqty)
		#///////////////////////////2

	#if newqty <= Dose:
	#	lcd.message("Youre running out of pills \n Head to the pharmacy")

	#else:
		moror1_down()

		lcd.clear()

def conv(pleaseetime):

	newtime = pleaseetime * 3600

	return newtime



while True:

	#time.sleep(conv(pilltime2))
	time.sleep(pilltime2)
	capstone()
	pilltime2 = Update_Capstone()




