# try :
#     n = int(input())
#     m = int(input())
#
#     result = n/m
#     print(result)
# except ZeroDivisionError:
#     print("m not be 0")
# except ValueError:
#     print("input wrtite value")
# finally:
#     print("Sucess")

#--------------------------------------------
n = 10
m = 2
try :
    print(int(n/m))
except Exception as error:
    print(error)