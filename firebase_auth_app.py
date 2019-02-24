import pyrebase as pb
import config as firebase_config
from flask import *

#intialize flask
app=Flask(__name__)

#initialize the firebase
firebase=pb.initialize_app(firebase_config.config)
auth=firebase.auth()

@app.route("/",methods=["POST","GET"])
def index():
	if request.method=="POST":
		email=request.form['email']
		password=request.form['pass']
		print(email,password)
		try:
			user=auth.sign_in_with_email_and_password(email,password);
			return render_template("index.html",success_login="login success")
		except:
			return render_template("index.html",us="email or password is wrong")

	return render_template("index.html")
if __name__=="__main__":
	app.run(debug=True,port=5003,host="localhost")
