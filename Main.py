from Perceptron import Perceptron
from Point import Point

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

# ask the brain to guess the correct output and if it fails then don't count towards accuracy
for x in range(0, 500):
    guess = brain.guess([points[x].x, points[x].y])
    if guess == points[x].label:
        numberCorrect = numberCorrect + 1

print('Perceptron Accuracy is: ' + str((numberCorrect / 500) * 100))
