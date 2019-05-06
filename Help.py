from firebase import firebase
import schedule
import time

firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)
datarefresh = 0
 
def Update():

	pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

	pilltime2 = int(pillhour)

def Work():
	print ("please")

schedule.every(datarefresh).minutes.do(Update)
schedule.every(pilltime2).minutes.do(Work)

while True:

	schedule.run_pending()
	time.sleep(1)
