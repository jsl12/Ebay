import sys
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from accounts import PRODUCTION_APPID
from ebay_processing import response_to_dataframe
import os
import search_queries

# Get the search query from the command line.
query_arg = sys.argv[1]

# Add error checking for empty string.

# Converts the query argument into a variable called query
exec('query = search_queries.' + query_arg.lower())

# Add error checking to make sure query_arg matches something and that query isn't an empty string.

try:
    api = Finding(appid=PRODUCTION_APPID, config_file=None)
    response = api.execute('findCompletedItems', query)
    df = response_to_dataframe(response)
    print(df.head())
    df.to_excel(
        'Results_' + query_arg + '.xlsx',
        sheet_name='Results',
        index=False
    )
except ConnectionError as e:
    print(e)
    print(e.response.dict())
