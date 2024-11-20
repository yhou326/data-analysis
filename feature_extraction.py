import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FeatureExtractor:
    def get_feature(self, csvData):
        rainLevel = pd.read_csv(csvData, dtype='object')
        currentMonth = '202101'
        lastMonth = '202202'
        monthList =[]
        date = datetime.strptime(currentMonth, '%Y%m')
        while date.strftime('%Y%m') < lastMonth:
            date = date + relativedelta(months=1)
            # make the date in String format
            monthList.append(date.strftime('%Y%m'))

        monthCol = []
        for month in monthList:
            monthCol.append(f'A_{month}')
        validCol = []
        for col in monthCol:
            if col in rainLevel.columns:
                validCol.append(col)
        print (rainLevel)
        print(validCol)

importFile = 'data/months.csv'
extractor = FeatureExtractor()
extractor.get_feature(importFile)