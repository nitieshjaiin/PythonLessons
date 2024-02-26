# multi-level inheritance

class Grand_father:
    def home(self):
        print("100 acres")

class Father(Grand_father):
    pass

class Son(Father):
    pass

Nitish = Grand_father()
Nitish.home()

KL = Grand_father()
KL.home()
