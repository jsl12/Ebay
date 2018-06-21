# Define the search criteria. Each list(?) defines a separate search.

# The original Hammond B3 and all of its variants, the B3 being the most desirable.
hammond_b3 = {
    'keywords': '+Hammond +(a100,"a-100",B2,"B-2",B3,"B-3",C2,"C-2",C3,"C-3")',
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

# Hammond B3 that's been "chopped" down to make it more portable.
hammond_chopped = {
    'keywords': '+Hammond +chopped',
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

# Original 2-speed Leslie speakers
leslie_tube = {
    'keywords': '+leslie +(122,122R,122RV,122V,147,147RV,145,142,251,245,242,351)',
    'categoryId': '180010',
    'itemFilter': [
        {
            'paramName': 'Currency',
            'paramValue': 'USD',
            'name': 'MaxPrice',
            'value': '2500'
        },
        {
            'paramName': 'Currency',
            'paramValue': 'USD',
            'name': 'MinPrice',
            'value': '150'
        },
    ]
}

# Solid state Leslie speakers from the 70s, 80s. Made to take on the road.
leslie_solid_state = {
    'keywords': '+leslie +(760,330,860,825,820,770,771)',
    'categoryId': '180010',
    'itemFilter': [
        {
            'paramName': 'Currency',
            'paramValue': 'USD',
            'name': 'MaxPrice',
            'value': '2500'
        },
        {
            'paramName': 'Currency',
            'paramValue': 'USD',
            'name': 'MinPrice',
            'value': '150'
        },
    ]
}

# Italian B3 knockoff that's supposed to be the real deal.
viscount_legend = {
    'keywords': '+viscount +legend',
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