import random


class Point:
    def __init__(self, width, height) -> None:
        super().__init__()
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.label = self.calculateLabel()

    def calculateLabel(self) -> int:
        if self.x >= self.y:
            return 1
        else:
            return -1
