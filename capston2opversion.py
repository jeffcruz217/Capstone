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



ControlPin3 = [12,16,20,21]

ControlPin4 = [21,20,16,12]



ControlPin5 = [18,24,25,8]

ControlPin6 = [8,25,24,18]



photores = 23

photores2 = 9

photores3 = 10



please = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

pilltime2= int(please)

please2 = firebase.get('/Current Schedule/Darel Diaz/Hours2',None)

pilltime3= int(please2)

please3 = firebase.get('/Current Schedule/Darel Diaz/Hours3',None)

pilltime4= int(please3)



def quantity():
	quant = firebase.get('/Current Schedule/Darel Diaz/Qty2', None)
	quantity = int(quant)

	return quantity


def Update_Capstone():

	pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

	pilltime = int(pillhour)

	return pilltime

def Update_Capstone2():

	pillhour2 = firebase.get('/Current Schedule/Darel Diaz/Hours2',None)

	pilltime22 = int(pillhour2)

	return pilltime22

def Update_Capstone3():

	pillhour3 = firebase.get('/Current Schedule/Darel Diaz/Hours3',None)

	pilltime33 = int(pillhour3)

	return pilltime33


def rc_time(photores):
	count=0
	GPIO.setup(photores,GPIO.OUT)
	GPIO.output(photores,GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(photores,GPIO.IN)

	while (GPIO.input(photores) == GPIO.LOW):
		count += 1
	return count

def rc_time2(photores2):
	count=0
	GPIO.setup(photores2,GPIO.OUT)
	GPIO.output(photores2,GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(photores2,GPIO.IN)

	while (GPIO.input(photores2) == GPIO.LOW):
		count += 1
	return count

def rc_time3(photores3):
	count=0
	GPIO.setup(photores3,GPIO.OUT)
	GPIO.output(photores3,GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(photores3,GPIO.IN)

	while (GPIO.input(photores3) == GPIO.LOW):
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



def motor2_up():
	for pin3 in ControlPin3:
		GPIO.setup(pin3,GPIO.OUT)
		GPIO.output(pin3,0)

	seq3= [ [1,0,0,0],
	       [1,1,0,0],
	       [0,1,0,0],
	       [0,1,1,0],
	       [0,0,1,0],
	       [0,0,1,1],
	       [0,0,0,1],
	       [1,0,0,1] ]

	for i in range (512):
		for halfstep in range(8):
			for pin3 in range(4):
				GPIO.output(ControlPin3[pin3], seq3[halfstep][pin3])

			time.sleep(0.001)
	

def moror2_down():

	for pin4 in ControlPin4:
			GPIO.setup(pin4,GPIO.OUT)
			GPIO.output(pin4,0)

	seq4 = [ [1,0,0,0],
			 [1,1,0,0],
	 	 	 [0,1,0,0],
	 	 	 [0,1,1,0],
	 	 	 [0,0,1,0],
	 	 	 [0,0,1,1],
	 	 	 [0,0,0,1],
	 	 	 [1,0,0,1] ]

	for i in range (512):
		for halfstep in range(8):
			for pin4 in range(4):
				GPIO.output(ControlPin4[pin4], seq4[halfstep][pin4])
			time.sleep(0.001)



def motor3_up():
	for pin5 in ControlPin5:
		GPIO.setup(pin5,GPIO.OUT)
		GPIO.output(pin5,0)

	seq5= [ [1,0,0,0],
	       [1,1,0,0],
	       [0,1,0,0],
	       [0,1,1,0],
	       [0,0,1,0],
	       [0,0,1,1],
	       [0,0,0,1],
	       [1,0,0,1] ]

	for i in range (512):
		for halfstep in range(8):
			for pin5 in range(4):
				GPIO.output(ControlPin5[pin5], seq5[halfstep][pin5])

			time.sleep(0.001)
	

def moror3_down():

	for pin6 in ControlPin6:
			GPIO.setup(pin6,GPIO.OUT)
			GPIO.output(pin6,0)

	seq6 = [ [1,0,0,0],
			 [1,1,0,0],
	 	 	 [0,1,0,0],
	 	 	 [0,1,1,0],
	 	 	 [0,0,1,0],
	 	 	 [0,0,1,1],
	 	 	 [0,0,0,1],
	 	 	 [1,0,0,1] ]

	for i in range (512):
		for halfstep in range(8):
			for pin6 in range(4):
				GPIO.output(ControlPin6[pin6], seq6[halfstep][pin6])
			time.sleep(0.001)

		

def capstone():


	message_motor1 = firebase.get('/Current Schedule/Darel Diaz/Name1',None)
	message2_motor1 = firebase.get('/Current Schedule/Darel Diaz/Dose1',None)

	Dose = int(message2_motor1)

#/////////////////////////////////1
	
	motor1_up()


	lcd.message("Pill Name: " + message_motor1 + "\n" + "Take: " +  message2_motor1 + " pill")

	if rc_time(photores) > 10000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		

		#//////////////////////////////////2
		moror1_down()

		lcd.clear()
	

	else:
		newqty = 0 
		qty = quantity()
		newqty = qty - Dose

		if newqty <= Dose:
			lcd.message("Youre running out of pills \n Head to the pharmacy")

			lcd.clear()
		else:
			new = str(newqty)
			lcd.message("You have " + new + "pills" + "\n" + "of" + message_motor1)


		newqty = firebase.update('/Current Schedule/Darel Diaz/Qty2', None)

		moror1_down()

		lcd.clear()
		#///////////////////////////2

		


def capstone2():


	message_motor2 = firebase.get('/Current Schedule/Darel Diaz/Name2',None)
	message2_motor2 = firebase.get('/Current Schedule/Darel Diaz/Dose2',None)

	Dose = int(message2_motor2)

#/////////////////////////////////1
	
	motor2_up()


	lcd.message("Pill Name: " + message_motor2 + "\n" + "Take: " +  message2_motor2 + " pill")

	if rc_time(photores2) > 10000:
		time.sleep(5)
		lcd.clear()
		
		

		#//////////////////////////////////2
		moror2_down()

		lcd.clear()
	

	else:
		newqty = 0 
		qty = quantity()
		newqty = Dose - qty

		
		newqty = firebase.post('/Current Schedule/Darel Diaz/Qty1', None)

		moror2_down()

		#///////////////////////////2

	if newqty <= Dose:
		lcd.message("Youre running out of pills \n Head to the pharmacy")

	else:
		moror2_down()

		lcd.clear()


def capstone3():


	message_motor3 = firebase.get('/Current Schedule/Darel Diaz/Name1',None)
	message2_motor3 = firebase.get('/Current Schedule/Darel Diaz/Dose1',None)

	Dose = int(message2_motor1)

#/////////////////////////////////1
	
	motor3_up()


	lcd.message("Pill Name: " + message_motor3 + "\n" + "Take: " +  message2_motor3 + " pill")

	if rc_time(photores3) > 10000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		

		#//////////////////////////////////2
		moror3_down()

		lcd.clear()
	

	else:
		newqty = 0 
		qty = quantity()
		newqty = Dose - qty

		
		firebase.post('/Current Schedule/Darel Diaz/Qty1', newqty)

		moror3_down()

		#///////////////////////////2

	if newqty <= Dose:
		lcd.message("Youre running out of pills \n Head to the pharmacy")

	else:
		moror3_down()

		lcd.clear()



def conv(pleaseetime):

	newtime = pleaseetime * 3600

	return newtime



while True:

	#time.sleep(conv(pilltime2))
	time.sleep(pilltime2)
	capstone()

	time.sleep(pilltime3 - pilltime2)
	capstone2()

	if(pilltime4 == pilltime2 == pilltime3):
		capstone3()

	else:
		time.sleep(pilltime4 - pilltime3)
		capstone3()

	pilltime2 = Update_Capstone()
	pilltime3 = Update_Capstone2()
	pilltime4 = Update_Capstone3()



