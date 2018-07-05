import sys
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import search_queries
from ebay_dataframe import response_to_dataframe


# Find "open listings" matching a predefined search query specified in the command line.
# The actual search queries are defined in search_queries.py
query_arg = sys.argv[1]

# Add error checking for empty string...

# Convert the query argument into a variable called 'query'
exec('query = search_queries.' + query_arg.lower())

# Add error checking to make sure query_arg actually matches one of the predefined queries
#   and that 'query' isn't an empty string.


try:
    # Query the API and store the results in a DataFrame.
    api = Finding()
    response = api.execute('findItemsAdvanced', query)
    df = response_to_dataframe(response)
    print(df.head())

    # Convert the results to an Excel spreadsheet.
    df.to_excel(
        'findItemsAdvanced_results.xlsx',
        sheet_name=query_arg.lower(),
        index=False
    )


except ConnectionError as e:
    print(e)
    print(e.response.dict())