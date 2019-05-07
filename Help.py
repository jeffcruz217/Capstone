from firebase import firebase
import schedule
import time

firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)
datarefresh = 0
 
def Update():

	pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

	pilltime2 = int(pillhour)
	print(pilltime2)
	
	return pilltime2

def Work():
	print ("please")


while True:
	pleasetime = Update()

	schedule.every(datarefresh).minutes.do(Update)

	schedule.every(pleasetime).minutes.do(Work)


	schedule.run_pending()
	#schedule.cancel_job(Work)


