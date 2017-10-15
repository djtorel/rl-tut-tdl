class Entity():
    """
    A generic object to repreent players, enemies, items, etc.
    """

    def __init__(self, x, y, char, color):
        """Init variables needed for object"""
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        """Move the entity by a given amount"""
        self.x += dx
        self.y += dy
