from abc import ABC, abstractmethod

from pandas import DataFrame


class BaseDataFetching(ABC):

    dataframe: DataFrame

    @abstractmethod
    def fetch_data(self ,path : str):
        pass