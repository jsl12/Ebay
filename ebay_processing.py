import pandas as pd

def response_to_dataframe(response):
    results = response.dict()['searchResult']['item']

    df = pd.DataFrame()
    df['Item ID'] = pd.Series([item['itemId'] for item in results])
    df['Title'] = pd.Series([item['title'] for item in results])
    df['Current Price'] = pd.Series([float(item['sellingStatus']['currentPrice']['value']) for item in results])
    df['Bid Count'] = pd.Series([int(item['sellingStatus'].get('bidCount', 0)) for item in results])
    df['Selling State'] = pd.Series([item['sellingStatus']['sellingState'] for item in results])
    df['Location'] = pd.Series([item['location'] for item in results])
    df['URL'] = pd.Series([item['viewItemURL'] for item in results])

    return df