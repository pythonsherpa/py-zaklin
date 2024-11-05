class A:
    def __init__(self):
        print("Greetings from class A")


class B(A):
    def __init__(self):
        print("Greetings from class B")
        super().__init__()


class C(A):
    def __init__(self):
        print("Greetings from class C")
        super().__init__()


class D(B, C):
    def __init__(self):
        super().__init__()


d = D()
print(type(d).__mro__)
