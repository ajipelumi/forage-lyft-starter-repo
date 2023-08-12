from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Battery(ABC):
    """ Battery interface. """
    @abstractmethod
    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        pass


class SplinderBattery(Battery):
    """ Splinder Battery class. """
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        """ Initialize the battery. """
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Get time since last service.
        time_since_last_service = self.current_date - self.last_service_date
        # Check if the battery needs service.
        if time_since_last_service > timedelta(days=2*365):
            # Return True.
            return True
        else:
            # Return False.
            return False


class NubbinBattery(Battery):
    """ Nubbin Battery class. """
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        """ Initialize the battery. """
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        """ Check if the service is needed. """
        # Get time since last service.
        time_since_last_service = self.current_date - self.last_service_date
        # Check if the battery needs service.
        if time_since_last_service > timedelta(days=4*365):
            # Return True.
            return True
        else:
            # Return False.
            return False
