import pandas as pd
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class JsonReading(BaseDataFetching):

    def fetch_data(self, path: str):
        self.dataframe = pd.read_json(path)
        print(self.dataframe.head())

    def __init__(self):
        super().__init__()

def main():
    jsonReading = JsonReading()
    jsonReading.fetch_data()


if __name__ == '__main__':
    main()