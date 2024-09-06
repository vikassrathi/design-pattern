from pizzaadon import pizzaadon


class cheese(pizzaadon):

    def get_price(self):
        return self.pizza.get_price +20

