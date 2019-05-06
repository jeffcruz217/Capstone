from firebase import firebase
import schedule
import time

firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)
datarefresh = 0
 
def Update():

	pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

	pilltime2 = int(pillhour)

	return pilltime2

def Work():
	print ("please")

schedule.every(datarefresh).minutes.do(Update)
schedule.every(Update).minutes.do(Work)

while True:

	schedule.run_pending()
	time.sleep(1)
