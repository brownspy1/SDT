class a:
    @staticmethod
    def taka():
        print(10000)
class b:
    @staticmethod
    def bari():
        print("3 tola ")
class c(a,b):
    pass
obj = c
obj.taka()
obj.bari()