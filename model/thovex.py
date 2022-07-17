from datetime import datetime

from model.car import Car


class Thovex(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        return self.engine.engine_should_be_serviced() and self.battery.battery_needs_service()
