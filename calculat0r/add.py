class Add():
    def __call__(self, a, b):
        if (type(a) is not int or type(b) is not int):
            raise TypeError('arguments must be of type int')

        return a + b
