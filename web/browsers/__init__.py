from abc import ABC, abstractmethod

from web.driver.driver import Driver


class WebBrowser(ABC):
    """Abstraction of a web browser."""

    @abstractmethod
    def driver(self) -> Driver:
        pass

    @abstractmethod
    def name(self) -> str:
        pass