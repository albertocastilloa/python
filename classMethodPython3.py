class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius

#A instance of Circle was created passing the argument to concstructor
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

#Circumference method was call
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())