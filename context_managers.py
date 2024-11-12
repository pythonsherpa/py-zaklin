# Good
file = open("zen.txt", "w")
file.write("Simple is better than complex")
file.close()

# Better
file = open("zen.txt", "w")
try:
    file.write("Simple is better than complex")
finally:
    file.close()

# Best
with open("zen.txt", "w") as file:
    file.write("Simple is better than complex")


class DemoContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, *args):
        print("Exiting the context")


with DemoContextManager():
    print("In the with statement")
