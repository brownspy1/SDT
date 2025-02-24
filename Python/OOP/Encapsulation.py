class login:
    def __init__(self,user_name,user_pass):
        self.name = user_name;
        self.__password = user_pass; ''' this is data encapsulason '''
    def login(self):
        print("Login successful!")
l = login("m","m")
l.login()