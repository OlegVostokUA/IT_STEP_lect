import turtle


### CASE 1 - Class, objects of class ###
class Rectangle:
    # static attributes
    color = 'Red'
    distance = 100

    # method object class
    def draw(self):
        turtle.pencolor(self.color)
        for i in range(4):
            turtle.forward(self.distance)
            turtle.right(90)
        turtle.exitonclick()


# objects
r1 = Rectangle()
r2 = Rectangle()

# change attributes 2 object
r2.color = 'Black'
r2.distance = 200

# call methods each object
# r1.draw()
# r2.draw()

### END CASE 1 ###
