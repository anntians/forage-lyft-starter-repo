from tire.tire import Tire
from utils import add_years_to_date


class CarriganTire(Tire):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        max = 0
        for i in self.tires:
            if i>max:
                max = i
        return max >=0.9

