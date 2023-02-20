import sys
import os
from sys import exit
import geopandas as gpd
from requests import Request
from owslib.wfs import WebFeatureService
import pyproj
import io

cwd = os.getcwd()
jsonDir = cwd + '/rajat/'
def listFiles():
    """
    list .json files
    """
    os.chdir(jsonDir)
    files = [f for f in os.listdir(jsonDir) if os.path.isfile(f)]
    files = [x for x in files if '.json' in x]
    files = [x for x in files if '~' not in x]
    files = sorted(files)
    return files

estateList = listFiles()
print(estateList)

# Metsakeskus WFS service
url = 'https://rajapinnat.metsaan.fi/geoserver/Avoinmetsatieto/ows'
wfs = WebFeatureService(url=url, version='1.1.0')

# which layer we want to fetch from the WFS service
layer_name = list(wfs.contents)[-3]
testList = ['99-403-8-56.json', '99-407-2-124.json']
standsList = []
for json in estateList:
    print(f'Fetching borders for {json}')
    estate = gpd.read_file(json)
    estate = estate.to_crs(3067)
    bbox = estate.bounds.iloc[0].to_list()
    tiedosto = wfs.getfeature(typename="Avoinmetsatieto:stand",
                              bbox=bbox,
                              )
    json = json[:-5]
    out = open(f'./{json}.gml', 'wb')
    out.write(tiedosto.read())
    out.close()

#for stands in standsList:
#    for json in estateList:
#        json = json[:-5]
#        print(f'writing {json} to file')
#        out = open(f'./{json}.gml', 'wb')
#    out.write(stands.read())
#    out.close()


# sourceCrs = 'epsg:4326'
# targetCrs = 'epsg:3067'
# 
# rajat = gpd.read_file('./rajat/143-403-1-96.json')
# print(rajat.bounds)
# print(type(rajat.bounds))
# rajabb = [rajat.bounds['miny'], rajat.bounds['minx'],
#           rajat.bounds['maxy'], rajat.bounds['maxx']]
# 
# #rajat = gpd.GeoDataFrame(rajat, crs=3067)
# rajat = rajat.to_crs(3067)
# bbox = rajat.bounds.iloc[0].to_list()
# print(bbox)
# #print(rajabb[1])
# 
# print(list(wfs.contents))
# 
# bbox3067 = [288992.8281530848471448,6869647.8752259304746985,289490.7372888674726710,6870058.5334552461281419]
# 
# print(wfs.get_schema('Avoinmetsatieto:stand'))
# 
# print(tiedosto)
# 
# out = open('./stands.gml', 'wb')
# out.write(tiedosto.read())
# out.close()
# 
# print(layer_name)
# print(list(wfs.contents))
