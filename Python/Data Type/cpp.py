class Cout:
    def __lshift__(self, msg):
        print(msg, end="")
        return self  # Allows chaining like cout << "Hello"

cout = Cout()