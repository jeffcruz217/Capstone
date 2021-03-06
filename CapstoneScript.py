#Pill Reminder, Capstone 2
#Jeffrey R. Cruz Rodriguez = S00914944
#Darel Diaz Ramos = S01045655

import RPi.GPIO as GPIO
import time
from time import sleep
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

photores2 = 10

photores3 = 9

buzzer = 3

GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,GPIO.LOW)


please = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

pilltime2= int(please)

please2 = firebase.get('/Current Schedule/Darel Diaz/Hours2',None)

pilltime3= int(please2)

please3 = firebase.get('/Current Schedule/Darel Diaz/Hours3',None)

pilltime4= int(please3)

def buzzer_beep():
	GPIO.output(buzzer,GPIO.HIGH)
	sleep(2)
	GPIO.output(buzzer,GPIO.LOW)
	sleep(2)
def buzzer_off():
	GPIO.output(buzzer,GPIO.LOW)

def quantity():
	quant = firebase.get('/Current Schedule/Darel Diaz/Qty1', None)
	quantity = int(quant)

	return quantity

def quantity2():
	quant2 = firebase.get('/Current Schedule/Darel Diaz/Qty2', None)
	quantity2 = int(quant2)

	return quantity2

def quantity3():
	quant3 = firebase.get('/Current Schedule/Darel Diaz/Qty3', None)
	quantity3 = int(quant3)

	return quantity3

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

	
	moror1_down()

	message_motor1 = firebase.get('/Current Schedule/Darel Diaz/Name1',None)
	message2_motor1 = firebase.get('/Current Schedule/Darel Diaz/Dose1',None)

	Dose = int(message2_motor1)

#/////////////////////////////////1
	

	buzzer_beep()
	lcd.message("Pill Name: " + message_motor1 + "\n" + "Take: " +  message2_motor1 + " pill")
	time.sleep(2)
	buzzer_off()

	if rc_time(photores) > 30000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		

		#//////////////////////////////////2
		motor1_up()

		lcd.clear()
	

	else:
		newqty = 0 
		qty = quantity()
		newqty = qty - Dose

		strqty = str(newqty)

		if newqty <= Dose:
			lcd.clear()
			lcd.message("Youre running out of pills \n Head to the pharmacy")

			lcd.clear()
		else:
			lcd.clear()
			new = str(newqty)
			lcd.message("You have " + new + "pills" + "\n" + "of" + message_motor1)

		#datatest = {"Qty1": newqty}
		firebase.put('/Current Schedule/Darel Diaz', "Qty1", strqty)

		motor1_up()

		lcd.clear()
		#///////////////////////////2

		

def capstone2():

	moror2_down()

	message_motor2 = firebase.get('/Current Schedule/Darel Diaz/Name2',None)
	message2_motor2 = firebase.get('/Current Schedule/Darel Diaz/Dose2',None)

	Dose2 = int(message2_motor2)

#/////////////////////////////////1
	
	buzzer_beep()
	lcd.message("Pill Name: " + message_motor2 + "\n" + "Take: " +  message2_motor2 + " pill")
	time.sleep(2)
	buzzer_off()

	if rc_time(photores2) > 30000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		

		#//////////////////////////////////2
		motor2_up()

		lcd.clear()
	

	else:
		newqty2 = 0 
		qty2 = quantity2()
		newqty2 = qty2 - Dose2

		strqty2 = str(newqty2)

		if newqty2 <= Dose2:
			lcd.clear()
			lcd.message("Youre running out of pills \n Head to the pharmacy")

			lcd.clear()
		else:
			lcd.clear()
			new2 = str(newqty2)
			lcd.message("You have " + new2 + "pills" + "\n" + "of" + message_motor2)

		#datatest2 = {"Qty2": newqty2}
		firebase.put('/Current Schedule/Darel Diaz', "Qty2", strqty2)

		motor2_up()

		lcd.clear()
		#///////////////////////////2

	
		


def capstone3():

	moror3_down()

	message_motor3 = firebase.get('/Current Schedule/Darel Diaz/Name3',None)
	message2_motor3 = firebase.get('/Current Schedule/Darel Diaz/Dose3',None)

	Dose3 = int(message2_motor3)

#/////////////////////////////////1
	
	

	buzzer_beep()
	lcd.message("Pill Name: " + message_motor3 + "\n" + "Take: " +  message2_motor3 + " pill")
	time.sleep(2)
	buzzer_off()

	if rc_time(photores3) > 20000:
		time.sleep(5)
		lcd.clear()
		lcd.message('Times up')
		

		#//////////////////////////////////2
		motor3_up()

		lcd.clear()
	

	else:
		newqty3 = 0 
		qty3 = quantity3()
		newqty3 = qty3 - Dose3

		strqty3 = str(newqty3)

		if newqty3 <= Dose3:
			lcd.clear()
			lcd.message("Youre running out of pills \n Head to the pharmacy")

			lcd.clear()
		else:
			lcd.clear()
			new3 = str(newqty3)
			lcd.message("You have " + new3 + "pills" + "\n" + "of" + message_motor3)

		#datatest3 = {"Qty3": newqty3}
		firebase.put('/Current Schedule/Darel Diaz', "Qty3", strqty3)

		motor3_up()

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
