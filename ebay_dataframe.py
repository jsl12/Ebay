import pandas as pd


def getvalueofitem(value):

        return value if value is not None else None


def response_to_dataframe(response):

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

    df = pd.DataFrame(columns=dfcols)

    results = response.dict()['searchResult']['item']

    for item in results:
        itemId = item['itemId']
        title = item['title']
        conditionDisplayName = item['condition']['conditionDisplayName']
        currentPrice = item['sellingStatus']['currentPrice']['value']
        sellingState = item['sellingStatus']['sellingState']
        bidCount = getvalueofitem(item['sellingStatus']['bidCount'])
        listingType = item['listingInfo']['listingType']
        bestOfferEnabled = item['listingInfo']['bestOfferEnabled']
        buyItNowAvailable = item['listingInfo']['buyItNowAvailable']
        startTime = item['listingInfo']['startTime']
        endTime = item['listingInfo']['endTime']
        watchCount = item['listingInfo']
        location = item['location']
        postalCode = item['postalCode']
        galleryURL = item['galleryURL']
        viewItemURL = item['viewItemURL']
        sellerUserName = item['sellerInfo']['sellerUserName']
        feedbackScore = item['sellerInfo']['feedbackScore']
        positiveFeedbackPercent = item['sellerInfo']['positiveFeedbackPercent']

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



