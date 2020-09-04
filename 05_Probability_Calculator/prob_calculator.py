import copy
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = list()
    [[self.contents.append(key) for i in range(value)] for key, value in kwargs.items()]

  def draw(self, numBalls):
    if numBalls > len(self.contents):
      return self.contents

    balls = list()
    for i in range(numBalls):
      selectedBall = random.choice(self.contents)
      balls.append(selectedBall)
      self.contents.remove(selectedBall)

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  success = 0
  expectedBalls = list()
  
  [[expectedBalls.append(key) for i in range(value)] for key, value in expected_balls.items()]

  for i in range(num_experiments):
    copiedHat = copy.deepcopy(hat)
    ballsDrawn = copiedHat.draw(num_balls_drawn)

    match = False
    for ball in set(expectedBalls):
      if expectedBalls.count(ball) <= ballsDrawn.count(ball):
        match = True
      else:
        match = False
        break

    if match:
      success += 1

  return success / num_experiments
