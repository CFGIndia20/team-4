# -*- coding: utf-8 -*-
"""
Contains the logic for taking input from different sources, 
storing it in db,
and returning a track id and url.
"""
from name_add_desc_separator import BreakDown

"""
    method mainExcalibur
    @params para, timestamp, source, phone_number, username
    return type dict({id, url})
"""
def mainExcalibur(para, timestamp=None, source=None, phone_number=None, username=None):
    """
        Takes the input from different sources, stores it and returns the track id and url.
    """
    name, location, descp = BreakDown(text=para)
    print(name, location, descp)
    return {'id': 'id', 'url': 'url'}

mainExcalibur('hi i am john doe. A tree near 23rd Street Bandra, Mumbai, MH 400001 has fallen.')