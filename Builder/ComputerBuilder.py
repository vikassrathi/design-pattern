"""
This is the abstact class which implemets the set and get methods

"""

from abc import  ABC,abstractmethod


class ComputerBuilder(ABC):
    def set_cpu(self,cpu):
        pass
    def set_gpu(self,gpu):
        pass

    def set_storage(self,storage):
        pass

    def set_ram(self,ram):
        pass

    def set_core(self,core):
        pass

    def build(self):
        pass