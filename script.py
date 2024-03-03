import pandas as pd



df = pd.read_excel('2021 Lineitems Cat IV, part 5 - 1707137367.xlsx')
date_columns = ['StartDate', 'EndDate']
df[date_columns] = df[date_columns].apply(pd.to_datetime, format='%d/%m/%Y').apply(lambda x: x.dt.strftime('%Y/%m/%d'))

# Add a new column based on the condition
df['value_gel'] = df.apply(lambda row: row['Value'] * 1000 if row['GEL'] == '000.ლარი' else row['Value'], axis=1)
df.to_csv('2021 Lineitems Cat IV, part 5 - 1707137367.csv', sep='|', index=False)