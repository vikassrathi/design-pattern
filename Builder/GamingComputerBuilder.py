
from  ComputerBuilder import ComputerBuilder
from Computer import  Computer
class GamingComputerBuilder(ComputerBuilder):

    def set_cpu(self,cpu):
        self.cpu=cpu
    def set_gpu(self,gpu):
        self.gpu=gpu

    def set_ram(self,ram):
        self.ram=ram
    def set_storage(self,storage):
        self.storage=storage
    def set_core(self,core):
        self.core=core

    def build(self):
        if self.cpu>1:
            return Computer(self.cpu, self.gpu, self.ram, self.storage, self.core)
