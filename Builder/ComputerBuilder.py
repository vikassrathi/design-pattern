"""
This is the abstact class which implemets the set and get methods

"""

from abc import  ABC,abstractmethod


class ComputerBuilder(ABC):
    def set_cpu(self):
        self.cpu=cpu