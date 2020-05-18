import pandas as pd
import glob
import datetime
import os
from datetime import timedelta, date

fileprefix = 'nssac-ncov-sd-'
startdate = date(2020, 4, 14)
is_map_data = False
if is_map_data:
    df_aggr = pd.DataFrame()
    num_days = 31
    for i in range(num_days):
        cur = startdate + timedelta(days=i)
        filename = fileprefix + cur.strftime("%m-%d-%Y") + '.csv'
        filename = os.path.join('nssac-ncov-data-country-state', filename)
        if os.path.isfile(filename):
            # print(filename, 'yes')
            df = pd.read_csv(filename)
            df = df[df.Region == 'USA']
            df_aggr = pd.concat([df_aggr, df])
    df_aggr = df_aggr.groupby('name').agg({'Confirmed':'sum', 'Deaths':'sum', 'Recovered':'sum', 'Region': 'any'})
    print(df_aggr)
    df_aggr[['Confirmed', 'Deaths', 'Recovered']].to_csv('static/data/deaths_30days.csv', header=True)
    df_aggr['Deaths'].to_csv('static/data/deaths_only_30days.csv', header=True)
    print(len(df), df.columns, len(df_aggr), df_aggr.columns)



# df_aggr = pd.DataFrame()
# files = glob.glob('nssac-ncov-data-country-state/*')
# for file_path in files:
#     if file_path.endswith('csv'):
#         df = pd.read_csv(file_path)
#         df = df[df.Region == 'USA']
#         # df = df[df.name == state]
#         df_aggr = pd.concat([df_aggr, df])
# # df_aggr = df_aggr.sort_values('Last Update')
# df_aggr = df_aggr.groupby('name').agg({'Confirmed':'sum', 'Deaths':'sum', 'Recovered':'sum', 'Region': 'any'})
# df_aggr[['Confirmed', 'Deaths', 'Recovered']].to_csv('static/data/covid19_usa_aggr_complete.csv', header=True)
# #     print(len(df), df.columns, len(df_aggr), df_aggr.columns)
# # df_aggr.to_csv('covid19_usa_complete.csv')
# print(df_aggr)

# concat all the files in a single file
# df_aggr = pd.DataFrame()
# files = glob.glob('nssac-ncov-data-country-state/*')
# for file_path in files:
#     if file_path.endswith('csv'):
#         df = pd.read_csv(file_path)
#         df = df[df.Region == 'USA']
#         # df = df[df.name == state]
#         df_aggr = pd.concat([df_aggr, df])
# # df_aggr = df_aggr.sort_values('Last Update')
# df_aggr.to_csv('static/data/covid19_usa_complete.csv', header=True, index=False)
# #     print(len(df), df.columns, len(df_aggr), df_aggr.columns)
# # df_aggr.to_csv('covid19_usa_complete.csv')
# print(df_aggr.index)



#####

df_aggr = pd.read_csv('static/data/covid19_usa_complete.csv')
df_aggr = df_aggr[df_aggr.name == 'New York']
df_aggr = df_aggr.sort_values('Last Update')
print(df_aggr)