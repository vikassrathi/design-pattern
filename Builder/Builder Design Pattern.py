# Guide:
# https://medium.com/@dilip.voleti/builder-design-pattern-62b4e0729408


from GamingComputerBuilder import GamingComputerBuilder
from Director import Director
if __name__=='__main__':
    gaming_computer_builder=GamingComputerBuilder()
    director=Director(gaming_computer_builder)
    gaming_pc=director.construct(2,1,'16gb','Inteli',2)
    print(gaming_pc)