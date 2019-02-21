class ShapeInterface:
    def draw(self):
        pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class Rectangle(ShapeInterface):
    def draw(self):
        print("Rectangle.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        elif type == 'sqaure':
            return Square()
        elif type == 'rectangle':
            return Rectangle()
        else:
            raise Exception("Couldn't find the {} factory class!!".format(type))


if __name__ == '__main__':

    f = ShapeFactory()

    c = f.getShape('circle')
    c.draw()

    r = f.getShape('rectangle')
    r.draw()

    v = f.getShape('vertex')
    v.draw()