
from abc import  abstractmethod,ABC

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_peremiter(self):
        pass



