from tire.tire import Tire
from utils import add_years_to_date


class OctoprimeTire(Tire):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        total = 0
        for i in self.tires:
            total+=i
        return total >= 3

