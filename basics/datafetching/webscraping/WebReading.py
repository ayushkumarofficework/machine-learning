import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

from basics.datafetching.base.BaseDataFetching import BaseDataFetching



class WebReading(BaseDataFetching):
    def __init__(self):
        super().__init__()

    dataframe : DataFrame
    def fetch_data(self):
        response = requests.get('https://www.ambitionbox.com/list-of-companies')
        soup = BeautifulSoup(response, 'lxml')