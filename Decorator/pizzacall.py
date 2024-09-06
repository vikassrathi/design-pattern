from basepizza import basepizza
from Decorator.addon import cheese,tomatos

if __name__ == '__main__':
    imput = "Base"
    Addons = "tomatos, cheese"

    adddons = Addons.split(", ")

    # Implement Builder..


    Pza = basepizza()
    tomato_pza = tomatos(Pza)

    print(tomato_pza.get_price())