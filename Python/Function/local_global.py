#Global scop
blance = 500
def chk():
    print(blance)
chk()

# def cal():
#     blance = blance-5
#     print(blance) //accebal na
# cal()
def gl():
    global blance
    blance = blance-5
    print(blance)
gl()

#local scop
def ami():
    name = "mahadi"
    print(name)
ami()
# print(name) // not accebal