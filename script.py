import pandas as pd



df = pd.read_excel('excelFIle.xlsx')
date_columns = ['StartDate', 'EndDate']
df[date_columns] = df[date_columns].apply(pd.to_datetime, format='%d/%m/%Y').apply(lambda x: x.dt.strftime('%Y/%m/%d'))

df['value_gel'] = df.apply(lambda row: row['Value'] * 1000 if row['GEL'] == '.000 ლარი' else row['Value'], axis=1)
df.to_csv('CSVFile.csv', sep='|', index=False)
