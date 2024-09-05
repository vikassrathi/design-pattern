

from shapefactory import  shapefactory
class ShapeClient:


    def __init__(self):
        shape_factory=shapefactory()

    def shape_client(self):
        shape_name=input('Enter The name of shape')
        shape=shapefactory.create_shape(shape_name)
        print(f'Area of {shape_name}',shape.calculate_area())
        print(f'Peremiter of {shape_name}',shape.calculate_peremiter())