import pandas as pd
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from ebay_dataframe import response_to_dataframe
from search_queries import hammond_b3

api = 'findCompletedItems'
query = 'hammond_b3'
excel_file = api + '-' + query + '.xlsx'

# Read the existing data from the Excel file into a DataFrame.
xlsx = pd.ExcelFile(excel_file)
df1 = pd.read_excel(xlsx, query, index_col=None, na_values=['NA'])
#print(df1.head())
#print(list(df1.columns))
#print(df1.itemId.values)

# Query the API and store the results into a second DataFrame.
try:
    api = Finding()
    response = api.execute('findCompletedItems', hammond_b3)
    # Note: I suspect that this API query is only returning the first 100 items.

    df2 = response_to_dataframe(response)
    #print(df2.head())

except ConnectionError as e:
    print(e)
    print(e.response.dict())

# Add only the newly found items to the first DataFrame.
for index,row in df2.iterrows():
    #print(row['itemId'])

    # Test to see if the itemId already exists in first DataFrame. If not, then add it.
    if row['itemId'] not in df1.itemId.values:
        print(row['itemId'])
        df1 = df1.append(row, ignore_index=True)

# Finally, write the updated first DataFrame back to the Excel file.
df1.to_excel(
    excel_file,
    sheet_name='hammond_b3',
    index=False
)

