from abc import ABC

from car import Car
from engine import Engine

class WilloughbyEngine(Engine):
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
