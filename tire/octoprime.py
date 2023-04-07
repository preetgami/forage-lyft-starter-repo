from tire import Tire
class Octoprime(Tire):
    def __init__(self,wear):
        self.wear=wear
    def tire_service(self):
        count=0
        for i in self.wear:
            count+=i
        if count>3:
            return True
        return False
