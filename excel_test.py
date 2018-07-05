import pandas as pd
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from ebay_dataframe import response_to_dataframe
from search_queries import hammond_b3

# Read the existing data
xlsx = pd.ExcelFile('findCompletedItems.xlsx')
df1 = pd.read_excel(xlsx, 'hammond_b3', index_col=None, na_values=['NA'])
#print(list(df1.columns))
print(df1.head())

try:
    # Query the API for new data and store the results in a DataFrame.
    api = Finding()
    response = api.execute('findCompletedItems', hammond_b3)
    df2 = response_to_dataframe(response)
    print(df2.head())

except ConnectionError as e:
    print(e)
    print(e.response.dict())


