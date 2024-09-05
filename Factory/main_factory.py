

from shapefactory import  shapefactory
class ShapeClient:


    def __init__(self):
        self.shape_name = input('Enter The name of shape')
        self.shape_factory=shapefactory(self.shape_name)

    def shape_client(self):
        shape=self.shape_factory.create_shape()
        print(f'Area of {self.shape_name}',shape.calculate_area())
        print(f'Peremiter of {self.shape_name}',shape.calculate_perimeter())



object=ShapeClient()
object.shape_client()
