from flask import Flask
# flask const takes the name of the current module(__name__) to be the argument
app=Flask(__name__)


# route fn  decorator , tells the app which url should  be accociated with that function
# app.route(rule,parameters)-> rule is url binding with function
# parameters list to be forwarded to the underlying rule
#  '/' this is url bounded with func helloWorld.
# when home page of web server is opened in the browser,
#  output of func is rendered



# routing  to help user remember  url of app
# used to bind the url to function, so we can acces the page
#  directly without navigating to the home page

# @app.route('/hello')
# routing to particular func through url

@app.route('/')
def helloWorld():
   return 'Hello World'



@app.route('/hello/<name>')
def helloWorld1(name):

    return 'Hello World {}'.format(name)

if __name__=='__main__':
    # app.debug=True
    app.run(debug=True)
    # app.run(debug=True)


    # run() method  of Flask class runs the app on local development server

    # app.run(host, port ,options)
    # local host and default port :5000


    # debug mode useful debugger to ta=rack errors
"""
     app  is started using run method, if app is under developmet ,it should be 
     restared manually for every change in the code
     """
# debug mode: server will reload itself

#  possible to build the url dynamically by adding variable parts
#  to the rule paramenter
# @app.route('/hello/<name>')