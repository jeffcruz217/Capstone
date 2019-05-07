from firebase import firebase
import schedule
import time

firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)
datarefresh = 0

please = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

pleasetime= int(please)

def Update():

	pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

	pilltime2 = int(pillhour)


	return pilltime2

def Work():
	print ("please")


while True:
	time.sleep(pleasetime)
	Work()
	pleasetime = Update()

	

	


	


