import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color in kwargs.keys():
      for amount in range(kwargs[color]):
        self.contents.append(color)

  def draw(self, amount):
    num_balls = len(self.contents)
    if amount > num_balls:
      amount = num_balls
    drawn = []
    for i in range(amount):
      drawn.append(self.contents.pop(random.randrange(len(self.contents))))
    return drawn
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_correct = 0
  for run in range(num_experiments):
    #reset hat
    temp = copy.deepcopy(hat)
    #run experiment
    result = temp.draw(num_balls_drawn)
    enough = True
    for i in expected_balls.keys():
      #if there is not enough balls of any color
      if not result.count(i) >= expected_balls[i]:
        enough = False
    if enough:
      num_correct += 1
  return num_correct/num_experiments
    