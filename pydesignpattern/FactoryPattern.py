"""
factory

    usage
    ---------------------------------------
    circle = ShapeFactory.create('Circle')
    circle.draw()

        output >>>
                    ()

    square = ShapeFactory.create('Square')
    square.draw()

        output >>>
                    ——
                   |  |
                    ——

"""


class ShapeFactory(object):

    class Shape(object):
        def __init__(self):
            super().__init__()
            pass

        def draw(self):
            print("""
            ————————
            |       |
            |    __________
            |    __________   |
            |       |
            ————————

            """)

    class Circle(Shape):
        def __init__(self):
            super().__init__()
            pass

        def draw(self):
            print("""
            ()
            """)

    class Square(Shape):
        def __init__(self):
            super().__init__()
            pass

        def draw(self):
            print("""
             ——
            |  |
             ——
            """)

    class Rectangle(Shape):
        def __init__(self):
            super().__init__()
            pass

        def draw(self):
            print("""
            ____________________
            |                   |
            |                   |
            |                   |
            ————————————————————
            """)

    @staticmethod
    def create(*args):
        print(ShapeFactory.__dict__)
        try:
            fuc = ShapeFactory.__dict__[args[0]]
        except KeyError:
            raise KeyError("unsupported class name: {}".format(args[0]))
        if fuc.__name__.startswith('_') or fuc.__name__ == 'create':
            raise KeyError("unsupported class name: {}".format(args[0]))
        else:
            return fuc()
