import pandas as pd
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class CsvReading(BaseDataFetching):



    def __init__(self):
        pass

    def fetch_data(self,path):
        self.dataframe = pd.read_csv(path)
        print(self.dataframe.head())


def main():
    csvReading = CsvReading()
    csvReading.fetch_data()


if __name__ == '__main__':
    main()