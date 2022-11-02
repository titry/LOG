import streamlit as st
import folium
from folium.plugins import Draw
from folium import IFrame
from streamlit_folium import st_folium
import base64
import os
import utils as utl

from PIL import Image
from PIL.ExifTags import TAGS
 
def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

@utl.find_picture
def add_picture(src: str, m):

    "## Try drawing some objects and then clicking on them"
    resolution, width, height = 30, 5, 5
    

    image_temp = Image.open(src)
    info = image_temp._getexif()
    image_temp.close()

    # print(info)

    tagLabel = {}
    try:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            tagLabel[decoded] = value
        exifGPS = tagLabel["GPSInfo"]
    except KeyError:
        return
    Lat = get_decimal_from_dms(exifGPS[2], exifGPS[1])
    Lon = get_decimal_from_dms(exifGPS[4], exifGPS[3])
    print(Lat, Lon)

    with open(src, "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())


    html = f'<img width="100%" src="data:image/png;base64, {image_as_base64.decode("utf-8")}" />'
    iframe = IFrame(html, width=(width*resolution)+20, height=(height*resolution)+20)
    popup = folium.Popup(iframe, max_width=2650)
    marker = folium.Marker(location=[Lat, Lon], popup=popup)
    marker.add_to(m)

def load_view():
    m = folium.Map(location=[36, 128], zoom_start=5)
    
    Draw(export=True).add_to(m)
    
    add_picture(m)

    output = st_folium(m, width = 700, height=500)