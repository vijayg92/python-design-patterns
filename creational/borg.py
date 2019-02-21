class Borg:

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__=='__main__':
    x = Borg()
    y = Borg()
    print(x == y)
    x.val = "Hello"
    y.val = "World"
    print(x.val, y.val)