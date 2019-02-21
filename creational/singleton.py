class Singleton:

    __instance = None

    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


if __name__=='__main__':
    a = Singleton()
    a.val = 'Hello'
    print(a.val)

    b = Singleton()
    b.val = 'World'
    print(b.val)

    print(" ")
    print(a.val)
    print(a==b)