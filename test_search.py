# testing pull request into zoltan57

import importlib
import sys
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from accounts import PRODUCTION_APPID
from ebay_processing import response_to_dataframe
from pprint import pprint



# Use a variable to refer to the query source and the output files
#  to make it easier to manage multiple queries.
#query_src = 'HammondB3'
query_src = sys.argv[1]
query_filename =  'query_' + query_src



query_file = importlib.import_module(query_filename)

try:
    api = Finding(appid=PRODUCTION_APPID, config_file=None)
    response = api.execute('findCompletedItems', query_file.query)
    df = response_to_dataframe(response)
    print(df.head())
    df.to_excel(
        'Results_' + query_src + '.xlsx',
        sheet_name='Results',
        index=False
    )
except ConnectionError as e:
    print(e)
    print(e.response.dict())

# Perform a case insensitive search for the query file name.
def find_sensitive_path(dir, insensitive_path):

    insensitive_path = insensitive_path.strip(os.path.sep)

    parts = insensitive_path.split(os.path.sep)
    next_name = parts[0]
    for name in os.listdir(dir):
        if next_name.lower() == name.lower():
            improved_path = os.path.join(dir, name)
            if len(parts) == 1:
                return improved_path
            else:
                return find_sensitive_path(improved_path, os.path.sep.join(parts[1:]))
    return None
    
