import pyrebase as pb
import config

#initialize the firebase
firebase=pb.initialize_app(config.config)
email="jitendra193266@gmail.com"
password="123456"
#--------------------Auth---------------------------------#
auth=firebase.auth()

#creates user with email and password
user=auth.create_user_with_email_and_password(email,password);
print("Created Account")

#sending verification email
print("Verification mail is sending")
auth.send_email_verification(user['idToken'])

#sign-in with email and password
user=auth.sign_in_with_email_and_password(email,password);
print("Signed in")

#resetting password
auth.send_password_reset_email(email)

#view user account info
info=auth.get_account_info(user['idToken'])
print(info)
