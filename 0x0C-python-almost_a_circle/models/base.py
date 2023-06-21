"""a new class"""


class Base():
    """base class of the project"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
