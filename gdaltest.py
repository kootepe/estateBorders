from owslib.ogcapi.features import Features
from osgeo import gdal
from owslib import openURL
import json

apiKey = '3ab64aed-4375-4586-bfe7-fe9a7f580c03'


#rajat = Features('https://avoin-paikkatieto.maanmittauslaitos.fi/kiinteisto-avoin/simple-features/v3')
rajat =openURL('https://avoin-paikkatieto.maanmittauslaitos.fi/kiinteisto-avoin/simple-features/v3', username = apiKey)

tilarajat = rajat.collection('PalstanSijaintitiedot')

tilarajat_queryables = rajat.collection_queryables('PalstanSijaintitiedot')

tilarajat_items = tilarajat.collection_items('PalstanSijaintitiedot')

tilarajat_features = tilarajat_items['kiinteistotunnuksenEsitysmuoto']

#/PalstanSijaintitiedot/items?kiinteistotunnuksenEsitysmuoto=230-405-9-325')

query_url = 'https://avoin-paikkatieto.maanmittauslaitos.fi/kiinteisto-avoin/simple-features/v3/collections/PalstanSijaintitiedot/items?kiinteistotunnuksenEsitysmuoto=230-405-9-325'

