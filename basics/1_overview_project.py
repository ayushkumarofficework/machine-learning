import pandas as pd



dataset = pd.read_csv('..\\datasets/train.csv', encoding='ISO-8859-1')
print(dataset.info())