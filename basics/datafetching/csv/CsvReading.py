import pandas as pd
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class CsvReading(BaseDataFetching):

    dataframe : DataFrame

    def __init__(self):
        pass

    def fetch_data(self):
        self.dataframe = pd.read_csv('..\\..\\..\\datasets\\train.csv',encoding='ISO-8859-1')
        print(self.dataframe.head())


def main():
    csvReading = CsvReading()
    csvReading.fetch_data()


if __name__ == '__main__':
    main()