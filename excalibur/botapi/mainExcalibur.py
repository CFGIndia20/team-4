# -*- coding: utf-8 -*-
"""
Contains the logic for taking input from different sources, 
storing it in db,
and returning a track id and url.
"""
from .name_add_desc_separator import BreakDown
from .textClassification import textClassifier
# from .models import Complaint
# from .api.serializers import ComplaintListSerializer
from .categories import category
import json
import requests
from datetime import datetime

"""
    method mainExcalibur
    @params para, timestamp, source, phone_number, username
    return type dict({id, url})
"""
def mainExcalibur(para, timestamp=datetime.now(), source="WH", phone_number=None, username=None):
    """
        Takes the input from different sources, stores it and returns the track id and url.
    """
    # Extraction of location
    l = BreakDown(text=para)
    name = l[0]
    location = l[1]
    descp = l[2]

    # Classifying into a category
    category_id = textClassifier(descp)

    # Posting on DB
    data = {
        'location' : location,
        'description' : descp,
        'category' : str(category_id),
        'timestamp' : str(timestamp),
        'source' : source,
        'phonenumber':str(phone_number),
        'username' : username,
    }
    url = 'http://127.0.0.1:8000/api/botapi/post/'
    x = requests.post(url, data = json.dumps(data), headers = {'Content-Type' : 'application/json'})
    
    x = x.json()
    # return "Thank you for posting the complain. Your complaint id is `x` {}. Your complaint id is For more details visit {}.".format(str(x["track_id"]), str(x["url"]))
    return {'id': x['track_id'], 'url': x['url']}

# x = mainExcalibur('hi i am John Doe. A tree near 1245 22nd street Bandra, Mumbai, MH 400001 has fallen.')
# print(x)