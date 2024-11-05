class Shape:
    def draw(self):
        print("drawing...")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


r = Rectangle(10, 20)
print(r.area())
r.draw()
s = Square(10)
print(s.area())
s.draw()


class ClothingItem:
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def print_color(self):
        print(self.color)


class Shirt(ClothingItem):
    def __init__(self, color, material, buttons):
        super().__init__(color, material)
        self.buttons = buttons


s = Shirt("black", "cotton", True)
s.print_color()


