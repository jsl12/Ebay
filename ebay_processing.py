import pandas as pd

def response_to_dataframe(response):
    results = response.dict()['searchResult']['item']
    df = pd.DataFrame({
        'Item ID': [item['itemId'] for item in results],
        'Title': [item['title'] for item in results],
        'Current Price': [float(item['sellingStatus']['currentPrice']['value']) for item in results]
    })
    return df