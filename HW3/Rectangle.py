#Chat prompts
#I'm coding a class in python right now and I keep getting this output when I try to print a new object using that class: <__main__.Rectangle object at 0x79ea75794d70>
#Do I have to use the str function in every class?
#If my homework asks for a method that calculates the area of the rectangle, would this work?

#     def __str__(self):
#         return f"{self.length} X {self.width} = {self.length * self.width}"

# It prints the area, but I don't know if this counts as a method. Please do not just give me the answer if I am wrong, rather help me understand if there is a difference between my code and a method.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # def __str__(self):
    #     return f"{self.length} X {self.width} = {self.length * self.width}"
    
    def calculate_area(self):
        area = self.length * self.width
        return area


rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()
print(area)
