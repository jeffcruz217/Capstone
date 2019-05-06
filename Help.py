from firebase import firebase
firebase = firebase.FirebaseApplication('https://pillreminder2-c8807.firebaseio.com/',None)

pillhour = firebase.get('/Current Schedule/Darel Diaz/Hours1',None)

print(pillhour,"is of type", type(pillhour))