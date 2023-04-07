from abc import ABC

from car import Car
from engine import Engine


class CapuletEngine(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
