# Web automation - Selenium
# Page - you're going to automate

class LoginPage:
    email = None
    password = None

    def __init__(self, username, pwd):
        self. email = username
        self.password = pwd

    def LoginConfirmation(self):
        if self.password == "Pass24":
            print("Access Granted")
        else:
            print("Access Denied")


Nitish = LoginPage("nitishjain1490","Pass24")
Nitish.LoginConfirmation()

print("________")
Jain = LoginPage("nitish","test")
Jain.LoginConfirmation()
