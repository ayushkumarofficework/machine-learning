import pandas as pd
import requests
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class ApiReading(BaseDataFetching):
    def fetch_data(self , path : str):
        response = requests.request(method="GET", url=path)
        dataframe = pd.DataFrame(response.json())
        print(self.dataframe)

    def __init__(self):
        super().__init__()


