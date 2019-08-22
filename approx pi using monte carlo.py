
import random
import math

insidePoints = 0
totalPoints = int(input('''Enter the number of points to drop randomly.
    As the no. of points tends to infinity, the error in the value of pi tends to zero.
     (points > 1 million  maybe CPU intensive):
     '''))
# totalPoints = 10000000

for i in range(0, totalPoints):

    x = random.random()
    y = random.random()

    distance = math.sqrt(math.fabs((x - 0.5) ** 2 + (y - 0.5) ** 2))

    if distance <= 0.5:
        insidePoints += 1

pi = 4 * (insidePoints / totalPoints)

print ("With {} points the value of pi is approximated to be: {}".format(totalPoints, pi))

