import random

import numpy as np


class Perceptron:
    def __init__(self, numberOfInputs) -> None:
        super().__init__()
        self.weights = [None] * numberOfInputs
        self.initializeWeights(numberOfInputs)

    def initializeWeights(self, numberOfInputs):
        for x in range(0, numberOfInputs, 1):
            self.weights[x] = random.randint(-1, 1)

    def guess(self, inputs) -> int:
        weightSum = 0
        for x in range(0, len(inputs), 1):
            weightSum += inputs[x] * self.weights[x]
        return np.sign(weightSum)

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        for x in range(0,len(self.weights)):
            self.weights[x] += error * inputs[x]
