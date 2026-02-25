import pandas as pd
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class JsonReading(BaseDataFetching):
    dataframe: DataFrame

    def fetch_data(self):
        self.dataframe = pd.read_json('..\\..\\..\\datasets\\train.json')
        print(self.dataframe.head())

    def __init__(self):
        super().__init__()

def main():
    jsonReading = JsonReading()
    jsonReading.fetch_data()


if __name__ == '__main__':
    main()