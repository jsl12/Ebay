import sys
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import search_queries
from ebay_dataframe import response_to_dataframe


# Find listings matching a predefined search query specified in the command line.
# The possible api args: 'findCompletedItems' and 'findItemsAdvanced'
# The actual search queries are defined in search_queries.py
api_arg = sys.argv[1]
query_arg = sys.argv[2]

# For testing purposes only
#total = len(sys.argv)
#cmdargs = str(sys.argv)
#print("total: %d " % total)
#print("Args: %s " % cmdargs)
# End

# Add error checking for empty string...

# Convert the query argument into a variable called 'query'
exec('query = search_queries.' + query_arg.lower())

# Add error checking to make sure query_arg actually matches one of the predefined queries
#   and that 'query' isn't an empty string.


try:
    # Query the API and store the results in a DataFrame.
    api = Finding()
    response = api.execute(api_arg, query)
    df = response_to_dataframe(response)
    print(df.head())

    # Write the DataFrame to an Excel spreadsheet
    df.to_excel(
        api_arg + '-' + query_arg + '.xlsx',
        sheet_name=query_arg,
        index=False
    )

except ConnectionError as e:
    print(e)
    print(e.response.dict())



