class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        result = .5 * self.base * self.height
        print(result)

t1 = Triangle(10,20)
t1.calculate_area()

t1 = Triangle(20,30)
t1.calculate_area()




