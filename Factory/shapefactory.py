



from shapes import *


class shapefactory:

    def __init__(self,name):
        self.name=name

    def create_shape(self):
        if self.name=='Rectangle' or self.name=='rectangle':
            height=input('Enter Height of Rectangle')
            width=input('Enter Width of Rectangle')
            return Rectangle(int(height),int(width))

        elif self.name=='Circle' or self.name=='circle':
            Radius=input('Enter radius of the circle')
            return Circle(float(Radius))
        else:
            width=input('width of the square')
            return Square(int(width))

