from Decorator.pizza import pizza



class pizzaadon(pizza):

    def __init__(self,pizza):
        self.pizza=pizza

    def get_price(self):
        return  self.pizza.get_price
