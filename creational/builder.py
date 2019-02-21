from copy import deepcopy

class Car:

    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def clone(self):
        return deepcopy(self)

    def specification(self):
        print("Body: {}".format(self.__body.shape))
        print("Engine horsepower: {}".format(self.__engine.horsepower))
        print("Tire size: {}".format(self.__wheels[0].size))


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car


class BuilderInterface:

    def getWheel(self):
        pass

    def getEngine(self):
        pass

    def getBody(self):
        pass


class JeepBuilder(BuilderInterface):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


class NissanBuilder(BuilderInterface):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def getBody(self):
        body = Body()
        body.shape = "HatchBack"
        return body


if __name__== '__main__':

    mycar = Director()
    # Jeep Builder #
    mycar.setBuilder(JeepBuilder())
    jeep = mycar.getCar()
    jeep.specification()
    jeep1 = jeep.clone()
    jeep1.specification()

    # Nisan Builder #
    print()
    mycar.setBuilder(NissanBuilder())
    mycar.getCar().specification()