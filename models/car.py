from abc import ABC, abstractmethod
from models.engine import Engine, CapuletEngine, WilloughbyEngine, StermanEngine
from models.battery import Battery, SplinderBattery, NubbinBattery
from models.tire import Tire, CarriganTire, OctoprimeTire


class Serviceable(ABC):
    """ Serviceable interface. """
    @abstractmethod
    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        pass


class Car(Serviceable):
    """ Car class. """
    def __init__(self, engine: Engine, battery: Battery, tire: Tire) -> None:
        """ Initialize the car. """
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Check if the engine needs service.
        if self.engine.needs_service():
            # Return True.
            return True
        # Check if the battery needs service.
        elif self.battery.needs_service():
            # Return True.
            return True
        # Check if the tire needs service.
        elif self.tire.needs_service():
            # Return True.
            return True
        else:
            # Return False.
            return False


class CarFactory:
    """ Car Factory class. """
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        """ Create a Calliope car. """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        """ Create a Glissade car. """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear):
        """ Create a Palindrome car. """
        engine = StermanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        """ Create a Rorschach car. """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        """ Create a Thovex car. """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)
