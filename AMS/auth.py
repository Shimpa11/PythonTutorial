from flask import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pyrebase
app=Flask(__name__)


cred = credentials.Certificate("heartdiseaseprediction-4baa3-firebase-adminsdk-p4zc3-15c662fb6a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/")
def home():

    return render_template('HomeView.html')

@app.route("/login",methods=['GET','POST'])
def login():

    return render_template('LoginView.html')

@app.route("/signIn",methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
        name=request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        password = request.form['pwd1']
        repass = request.form['pwd2']
        if password == repass:

            db.collection("Register").document().set({
                "name":name,
                "gender":gender,
                "age":age,
                "email":email,
                "password":password
                })
        else:
           print("Password not matched")


    return render_template('SignInView.html')

@app.route("/aboutUs")
def prediction():

    return render_template('')



if __name__=='__main__':

    app.run(debug=True)

