import pandas as pd
import requests
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class ApiReading(BaseDataFetching):
    dataframe : DataFrame
    def fetch_data(self):
        response = requests.request(method="GET", url="http://127.0.0.1:8000/api/reading")
        dataframe = pd.DataFrame(response.json())
        print(self.dataframe)

    def __init__(self):
        super().__init__()


