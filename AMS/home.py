
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

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
auth=firebase.auth()
db=firebase.database()



# db.child("teacher-db").child("name").push({"name":"shimpa"})

from flask import Flask,render_template,request,url_for,redirect

# print(Flask.__version__)



app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/teacher_login",methods=['GET','POST'])
def teacherLogin():

        if request.method == 'POST':
             if request.form['submit'] == 'Login':
                name = request.form['textnames']
                db.child("teacher_DB").push(name)
                teacher_DB = db.child("teacher_DB").get()
                to = teacher_DB.val()

#
                sex = request.form['sex']
                db.child("teacher_DB").push(sex)
                teacher_DB = db.child("teacher_DB").get()
                to = teacher_DB.val()

                email = request.form['textname']
                db.child("teacher_DB").push(email)
                teacher_DB = db.child("teacher_DB").get()
                to = teacher_DB.val()

                pwd = request.form['psw']
                db.child("teacher_DB").push(pwd)
                teacher_DB = db.child("teacher_DB").get()
                to=teacher_DB.val()


                return render_template("success.html",t=to)

        return render_template("teacher_login.html")



@app.route("/student_login", methods=['GET','POST'])
def studentLogin():
    if request.method == 'POST':
        if request.form['register'] == 'Register':
            name = request.form['textnames']
            db.child("student_DB").push(name)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            fname = request.form['fathername']
            db.child("student_DB").push(fname)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            address = request.form['paddress']
            db.child("student_DB").push(address)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            pcode = request.form['pincode']
            db.child("student_DB").push(pcode)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            sex = request.form['sex']
            db.child("student_DB").push(sex)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            email = request.form['emailid']
            db.child("student_DB").push(email)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            dateofB = request.form['dob']
            db.child("student_DB").push(dateofB)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            dateofJ = request.form['doj']
            db.child("student_DB").push(dateofJ)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            mobile = request.form['mobileno']
            db.child("student_DB").push(mobile)
            student_DB = db.child("student_DB").get()
            to1 = student_DB.val()

            return render_template("success.html",t1=to1)

        elif request.form['reset']=='Reset':
            return render_template("reset.html")


    return render_template("student_login.html")

@app.route("/upload-image", methods=['GET','POST'])
def uploadImage():
    if request.method == 'POST':  # Just to Validate if user is uploading the file in POST Request
        if request.form['upload']=='Uplaod':

            file = request.files['upload']


            # db.child("images").push(file)
            file.save(file.filename)
            # return render_template('dataset.html',name=file.filename)
        # return render_template('dataset.html')



@app.route("/parent_login",methods=['GET','POST'])
def parentLogin():
    if request.method == 'POST':
        if request.form['submit'] == 'Login':
            name = request.form['textnames']
            db.child("parent_DB").push(name)
            parent_DB = db.child("parent_DB").get()
            to2 = parent_DB.val()


            email = request.form['textname']
            db.child("parent_DB").push(email)
            parent_DB = db.child("parent_DB").get()
            to2 = parent_DB.val()

            pwd = request.form['psw']
            db.child("parent_DB").push(pwd)
            parent_DB = db.child("parent_DB").get()
            to2 = parent_DB.val()

            return render_template("success.html", t=to2)

    return render_template("parent_login.html")




if __name__ == '__main__':
    app.run(debug=True,port=5004)