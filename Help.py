from firebase import firebase
firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)

pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

pilltime2 = int(pillhour)

def Work():
	print ("please")

schedule.every(pilltime2).minutes.do(Work)