from abc import ABC

from battery.battery import Battery

from datetime import datetime



class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
