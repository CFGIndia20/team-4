#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS


# In[30]:


#getting the metadata
from PIL import Image

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

exif = get_exif('IMG_20200725_193746782.jpg')
print(exif)


# In[25]:


def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

exif = get_exif('IMG_20200725_193746782.jpg')
labeled = get_labeled_exif(exif)
print(labeled)


# In[26]:



def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

exif = get_exif('IMG_20200725_193746782.jpg')
geotags = get_geotagging(exif)
print(geotags)


# In[35]:


def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
    result = {
        "lat": lat, 
        "lon": lon
    }
    json_object = json.dumps(result)
    return json_object


exif = get_exif('IMG_20200725_193746782.jpg')
geotags = get_geotagging(exif)
print(get_coordinates(geotags))


# In[ ]:




