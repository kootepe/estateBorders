import os
import sys
import json
import requests
import pandas as pd
import numpy as np

tilarajat = pd.read_csv('./metsaanTilat.csv',
                        usecols=[0])

rajaLista = tilarajat['tunnus'].values.tolist()
rajaLista = sorted(rajaLista)

apiKey = '3ab64aed-4375-4586-bfe7-fe9a7f580c03'

for t in rajaLista:
    kiTu = t
    printThis = f'Downloading borders for {kiTu}'
    print(printThis)
    stuff = f'PalstanSijaintitiedot/items?kiinteistotunnuksenEsitysmuoto={kiTu}'
    api = f'https://avoin-paikkatieto.maanmittauslaitos.fi/kiinteisto-avoin/simple-features/v3/collections/{stuff}'
    filename = f'./rajat/{kiTu}.json'
    r = requests.get(api, auth=(apiKey, ''))
    with open(filename, 'wb') as f:
        f.write(r.content)
