from basics.datafetching.csv.CsvReading import CsvReading
from dataanalysis.base.BaseDataAnalysis import BaseDataAnalysis


class UnivariateAnalysis(BaseDataAnalysis):
    def gatherData(self):
        self.baseDataFetching = CsvReading()
        self.baseDataFetching.fetch_data(path='..\\datasets\\titanic_dataset.csv')

    def analyse(self):
        print(self.getShapeOfData())
        print(self.getInfoOfData())
        print(self.getCorrelationOfData())
        pass

    def __init__(self):
        super(UnivariateAnalysis, self).__init__()







def univariateAnalysis():
    univariateAnalysis = UnivariateAnalysis()
    univariateAnalysis.start_analysis()

if __name__ == '__main__':
    univariateAnalysis()
