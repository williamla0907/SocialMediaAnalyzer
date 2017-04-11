from pyrebase import initialize_app

#Firebase credentials
config = {
  "apiKey": "AIzaSyBhm88HaSINpFkJaftIQ6qi4bNLsZGc9Pc",
  "authDomain": "tweetsdb-c46cf.firebaseapp.com",
  "databaseURL": "https://tweetsdb-c46cf.firebaseio.com/",
  "storageBucket": "tweetsdb-c46cf.appspot.com",
}

#Firebase Auth and get database method
firebase = initialize_app(config)
db = firebase.database()

def getKeywordsFromDatabase():
    keywords_obj = db.child('keyword').shallow().get()
    keywords = keywords_obj.val()
    return keywords

def getData(keyword):
    data_obj = db.child('keyword').child(keyword).get()
    data = data_obj.val()['text']
    data = data.split(';')
    return data