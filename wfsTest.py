import geopandas as gpd
from requests import Request
from owslib.wfs import WebFeatureService
import pyproj
import io

sourceCrs = 'epsg:4326'
targetCrs = 'epsg:3067'

rajat = gpd.read_file('./rajat/143-403-1-96.json')
print(rajat.bounds)
print(type(rajat.bounds))
rajabb = [rajat.bounds['miny'], rajat.bounds['minx'],
          rajat.bounds['maxy'], rajat.bounds['maxx']]

#rajat = gpd.GeoDataFrame(rajat, crs=3067)
rajat = rajat.to_crs(3067)
bbox = rajat.bounds.iloc[0].to_list()
print(bbox)
#print(rajabb[1])
url = 'https://rajapinnat.metsaan.fi/geoserver/Avoinmetsatieto/ows'

wfs = WebFeatureService(url=url, version='1.1.0')

layer_name = list(wfs.contents)[-3]
print(list(wfs.contents))

bbox3067 = [288992.8281530848471448,6869647.8752259304746985,289490.7372888674726710,6870058.5334552461281419]

print(wfs.get_schema('Avoinmetsatieto:stand'))

tiedosto = wfs.getfeature(typename="Avoinmetsatieto:stand",
                          bbox=bbox,
                          )
print(tiedosto)

out = open('./stands.gml', 'wb')
out.write(tiedosto.read())
out.close()

print(layer_name)
print(list(wfs.contents))
