from abc import ABC, abstractmethod
from typing import List


class Tire(ABC):
    """ Tire interface. """
    @abstractmethod
    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        pass


class CarriganTire(Tire):
    """ Carrigan Tire class. """
    def __init__(self, tire_wear: List[float]) -> None:
        """ Initialize the tire. """
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Check if the tire needs service.
        for tire in self.tire_wear:
            if tire >= 0.9:
                # Return True
                return True
        # Return False
        return False


class OctoprimeTire(Tire):
    """ Octoprime Tire class. """
    def __init__(self, tire_wear: List[float]) -> None:
        """ Initialize the tire. """
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Check if the tire needs service.
        # Get the sum of the tire wear.
        tire_wear_sum = sum(self.tire_wear)
        if tire_wear_sum >= 3:
            # Return True
            return True
        # Return False
        return False
