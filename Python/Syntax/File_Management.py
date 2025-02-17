##writing data in file
# with open("file.txt",'w') as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\ni like programming in java")

#replace java with python
def replace(old,new):
    with open("file.txt", 'r') as f:
        data = f.read()
    new_data = data.replace(old, new)
    with open("file.txt", "w") as f:
        f.write(new_data)

# find learning in file
def word_find(find):
    with open("file.txt", "r") as f:
        data = f.read()
        if find in data:
            print("Found")
        else:
            print("Not Founs!")

#find word by line
def line_found(word):
    with open("file.txt",'r') as f:
        line = f.readline()
        line_no = 1
        try:
            while line:
                if word in line:
                    print(line_no)
                    return
                line += f.readline()
                line_no += 1
            print("Not found")
            return
        except Exception as error:
            print(error)
# line_found("like")
#find numbber evan ot odd from file
def number_chack(type = "even"):
    with open("file.txt","r") as f:
        data = [int(num) for num in f.read().split(",")]
        even = 0
        odd  = 0
        for i in data:
            if i%2 == 0:
                even +=1
            else:
                odd+=1
        if type == "odd":
            return odd
        elif type == "even":
            return even
print(number_chack())