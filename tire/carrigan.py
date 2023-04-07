from tire import Tire

class Carrigan(Tire):
    def __init__(self,wear):
        self.wear=wear
    def tire_service(self):
        count=0
        for i in self.wear:
            if i>=0.9:
                count+=1

            
        if count>=1:
            return True
        return False
