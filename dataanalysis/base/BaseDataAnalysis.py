from abc import ABC, abstractmethod

from basics.datafetching.base.BaseDataFetching import BaseDataFetching


class BaseDataAnalysis(ABC):

    baseDataFetching : BaseDataFetching

    @abstractmethod
    def gatherData(self):
        pass

    @abstractmethod
    def analyse(self):
        pass

    def start_analysis(self):
        self.gatherData()
        self.analyse()

    def getShapeOfData(self):
        print("Shape of Data --------------------------------")
        return self.baseDataFetching.dataframe.shape

    def getInfoOfData(self):
        print("Info of Data --------------------------------")
        return self.baseDataFetching.dataframe.info

    def getCorrelationOfData(self):
        print("Correlation of Data --------------------------------")
        return self.baseDataFetching.dataframe.corr
