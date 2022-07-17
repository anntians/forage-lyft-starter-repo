from abc import ABC, abstractmethod

from Serviceable import Serviceable

class Car(ABC, Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
