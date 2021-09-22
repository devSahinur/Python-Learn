class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(A,B):
    pass
    # A- display1()
    # B- display2()
    def display(self):
        print("I am inside C class")

ob1 = C()
ob1.display()