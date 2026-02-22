from abc import ABC, abstractmethod

from pandas import DataFrame


class BaseDataFetching(ABC):
    @abstractmethod
    def fetch_data(self) -> DataFrame:
        pass