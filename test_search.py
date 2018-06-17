from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from accounts import PRODUCTION_APPID

from pprint import pprint

try:
    api = Finding(appid=PRODUCTION_APPID, config_file=None)
    query = {
        'keywords': '+Hammond +(a100,""a-100"",B2,""B-2"",B3,""B-3"",C2,""C-2"",C3,""C-3"")',
        'categoryId': '180010',
        'itemFilter': [
            {
                'paramName': 'Currency',
                'paramValue': 'USD',
                'name': 'MaxPrice',
                'value': '15000'
            },
            {
                'paramName': 'Currency',
                'paramValue': 'USD',
                'name': 'MinPrice',
                'value': '500'
            },
        ]
    }

    response = api.execute('findItemsAdvanced', query)
    pprint(response.dict())
except ConnectionError as e:
    print(e)
    print(e.response.dict())