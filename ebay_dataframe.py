import pandas as pd


def getvalueofitem(value):

    return value if value is not None else None

def isNotEmpty(s):

    return bool(s and s.strip())

def response_to_dataframe(response):

    # Define column headers.
    dfcols = [
        'itemId',
        'title',
        'conditionDisplayName',
        'currentPrice',
        'sellingState',
        'bidCount',
        'listingType',
        'bestOfferEnabled',
        'buyItNowAvailable',
        'startTime',
        'endTime',
        'watchCount',
        'location',
        'postalCode',
        'galleryURL',
        'viewItemURL',
        'sellerUserName',
        'feedbackScore',
        'positiveFeedbackPercent',
    ]

    # Make the column headers the first row in a DataFrame.
    df = pd.DataFrame(columns=dfcols)


    # Get the search results
    results = response.dict()['searchResult']['item']

    # Parse out the interesting bits from the search results and add to the DataFrame.
    for item in results:
        itemId = item['itemId']
        title = item['title']
        conditionDisplayName = item['condition']['conditionDisplayName']
        currentPrice = float(item['sellingStatus']['currentPrice']['value'])
        sellingState = item['sellingStatus']['sellingState']
        try:
            bidCount = int(item['sellingStatus']['bidCount'])
        except:
            bidCount = 0
        listingType = item['listingInfo']['listingType']
        bestOfferEnabled = item['listingInfo']['bestOfferEnabled']
        buyItNowAvailable = item['listingInfo']['buyItNowAvailable']
        startTime = pd.to_datetime(item['listingInfo']['startTime'])
        endTime = pd.to_datetime(item['listingInfo']['endTime'])
        try:
            watchCount = int(item['listingInfo']['watchCount'])
        except:
            watchCount = 0
        location = item['location']
        try:
            postalCode = item['postalCode']
        except:
            postalCode = ''
        galleryURL = item['galleryURL']
        viewItemURL = item['viewItemURL']
        sellerUserName = item['sellerInfo']['sellerUserName']
        feedbackScore = item['sellerInfo']['feedbackScore']
        positiveFeedbackPercent = item['sellerInfo']['positiveFeedbackPercent']


        #
        dfrows = [
            itemId,
            title,
            conditionDisplayName,
            currentPrice,
            sellingState,
            bidCount,
            listingType,
            bestOfferEnabled,
            buyItNowAvailable,
            startTime,
            endTime,
            watchCount,
            location,
            postalCode,
            galleryURL,
            viewItemURL,
            sellerUserName,
            feedbackScore,
            positiveFeedbackPercent,
        ]

        df = df.append(pd.Series(dfrows, index=dfcols), ignore_index=True)

    return df



