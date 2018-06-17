from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from accounts import PRODUCTION_APPID

from pprint import pprint

try:
    api = Finding(appid=PRODUCTION_APPID, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'Python'})
    pprint(response.dict())
except ConnectionError as e:
    print(e)
    print(e.response.dict())