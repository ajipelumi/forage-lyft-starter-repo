from abc import ABC, abstractmethod


class Engine(ABC):
    """ Engine interface. """
    @abstractmethod
    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        pass


class CapuletEngine(Engine):
    """ Capulet Engine class. """
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        """ Initialize the engine. """
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Check if the engine needs service.
        if self.current_mileage - self.last_service_mileage > 30000:
            # Return True.
            return True
        else:
            # Return False.
            return False


class WilloughbyEngine(Engine):
    """ Willoughby Engine class. """
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        """ Initialize the engine. """
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Check if the engine needs service.
        if self.current_mileage - self.last_service_mileage > 60000:
            # Return True.
            return True
        else:
            # Return False.
            return False


class StermanEngine(Engine):
    """ Sterman Engine class. """
    def __init__(self, warning_light: bool) -> None:
        """ Initialize the engine. """
        self.warning_light = warning_light

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Check if the engine needs service.
        if self.warning_light:
            # Return True.
            return True
        else:
            # Return False.
            return False
