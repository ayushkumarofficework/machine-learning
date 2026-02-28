from basics.datafetching.csv.CsvReading import CsvReading
from dataanalysis.base.BaseDataAnalysis import BaseDataAnalysis


class BiVariateAnalysis(BaseDataAnalysis):
    def gatherData(self):
        self.baseDataFetching = CsvReading()
        self.baseDataFetching.fetch_data(path='..\\datasets\\titanic_dataset.csv')

    def analyse(self):
        pass

    def __init__(self):
        super(BiVariateAnalysis, self).__init__()

def bivariate_analysis():
    bivariate_analysis = BiVariateAnalysis()
    bivariate_analysis.start_analysis()

if __name__ == '__main__':
    bivariate_analysis()