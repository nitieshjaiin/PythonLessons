class Password:
    def __init__(self, pwd):
        self.__password = pwd
        self.public_var = 10

    def get_pwd(self, is_auth): # Get function used to access protected variable
        if is_auth:
            print(self.__password)
        else:
            print("Invalid Password")

    def set_pwd(self,password): # Set function used to set value to protected variable
        if len(password) > 10:
            self.__password = password
            print("Password is set", self.__password)
        else:
            print("Not allowed, weak password")


pwd = Password("Hacker123")
print(pwd.public_var)
pwd.get_pwd(True)
pwd.set_pwd("1234")
pwd.set_pwd(("NitishJain123"))