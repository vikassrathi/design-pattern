from pizzaadon import pizzaadon



class tomatos(pizzaadon):


    def get_price(self):
        return self.pizza.get_price()+10

