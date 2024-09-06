from abc import ABC , abstractmethod



class pizza(ABC):

    @abstractmethod
    def get_price(self):
        pass
    