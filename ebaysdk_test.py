import sys
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import search_queries


# Select a search query from the command line. The search queries are defined in
# search_queries.py
query_arg = sys.argv[1]
# Add error checking for empty string.
# Converts the query argument into a variable called query
exec('query = search_queries.' + query_arg.lower())
# Add error checking to make sure query_arg matches something and that query isn't an empty string.


try:
    api = Finding()
    response = api.execute('findCompletedItems', query)
    print(response.dict())

except ConnectionError as e:
    print(e)
    print(e.response.dict())