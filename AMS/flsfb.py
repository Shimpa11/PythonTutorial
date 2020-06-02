import pyrebase

config = {
  "apiKey": "AIzaSyAs3r17MHF_gswoT_MzvMROYx2C2HgN0pE",
  "authDomain": "amsr-d24c7.firebaseapp.com",
  "databaseURL": "https://amsr-d24c7.firebaseio.com",
  "projectId": "amsr-d24c7",
  "storageBucket": "amsr-d24c7.appspot.com",
  "messagingSenderId": "82823317595",
  "appId": "1:82823317595:web:e0c76f1f6a873c0976177e",
  "measurementId": "G-SQYRVES055"
}

firebase=pyrebase.initialize_app(config)
db=firebase.database()
# # db.child("names").push({"name":"shimpa"})
# # db.child("names").push({"name":"sethi","id":2,"dept":"ECE"})
#
db.child("names").child("id").remove()
db.child("names").remove()

