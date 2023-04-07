class CarFactory():
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        eng= CapuletEngine(current_mileage, last_service_mileage)
        battery=SpindlerBatter()