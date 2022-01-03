# 20.Write a Python program to using multiple inheritance.
class A:
    def __init__(self):
        self.name = 'John'
        self.age = 23

    def getName(self):
        return self.name


class B:
    def __init__(self):
        self.name = 'Richard'
        self.id = '32'

    def getName(self):
        return self.name


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def getName(self):
        return self.name


C1 = C()
print(C1.getName())
