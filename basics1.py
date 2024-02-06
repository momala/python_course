class Point:
   def __init__(self, x, y):
       # self refers to current object
       self.x = x
       self.y = y

   def move(self):
       print("move")

   def draw(self):
       print("draw")


point1 = Point(10, 20)
#point1.x = 10
print(point1.x)