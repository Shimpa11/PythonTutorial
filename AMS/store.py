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
storage=firebase.storage()
path_on_cloud="images/education.png"
path_local="avatar.png"

storage.child(path_on_cloud).put(path_local)
storage.child(path_on_cloud).download("new.png")