from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def battery_needs_service(self):
        pass
