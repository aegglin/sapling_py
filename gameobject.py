class GameObject:
    def __init__(self, position, sprite, speed):
        self.position = position
        self.sprite = sprite
        self.speed = speed

    def draw(self, surface):
        pass

    def update(self, surface):
        pass