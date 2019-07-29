from Perceptron import Perceptron
from Point import Point
import matplotlib.pyplot as plt
import numpy as np

brain = Perceptron(2)
inputs = [-1, 0.5]

width = 800
height = 800
points = [Point] * 500

# create a training data set of 500

for x in range(0, 500):
    points[x] = Point(width, height)

# train the perceptron on the training data
for x in range(0, 500):
    brain.train([points[x].x, points[x].y], points[x].label)

numberCorrect = 0

# create another 500 testing data
for x in range(0, 500):
    points[x] = Point(width, height)

data = np.zeros(shape=[500, 3], dtype=object)

# ask the brain to guess the correct output and if it fails then don't count towards accuracy
for x in range(0, 500):
    guess = brain.guess([points[x].x, points[x].y])
    if guess == points[x].label:
        numberCorrect = numberCorrect + 1
        data[x] = [points[x].x, points[x].y, 'green']
    else:
        data[x] = [points[x].x, points[x].y, 'red']

plt.scatter(data[:, 0], data[:, 1], marker='o', c=data[:,2])
plt.show()
print('Perceptron Accuracy is: ' + str((numberCorrect / 500) * 100))
