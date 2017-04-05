from pyrebase import initialize_app

#Firebase credentials
config = {
  "apiKey": "AIzaSyBr4jdeC3GoXYf1OiFqzzCHxD68FhloRkE",
  "authDomain": "socialmediaanalyzer-656b7.firebaseapp.com",
  "databaseURL": "https://socialmediaanalyzer-656b7.firebaseio.com",
  "storageBucket": "socialmediaanalyzer-656b7.appspot.com"
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