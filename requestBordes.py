"""
Ottaa sisään .csv tiedoston jossa on yhdessä sarakkeessa
kiinteistötunnuksia, tekee niistä listan ja lataa niiden kiinteistöjen
rajat MMLn OGC API Features palvelusta.
"""
import os
import sys
import requests
import pandas as pd

kiinteistotunnus = sys.argv

if len(kiinteistotunnus) > 1:
    for i in range(1, len(kiinteistotunnus)):
                   tunnusLista = kiinteistotunnus[1:]
else:
    tunnusDF = pd.read_csv('./metsaanTilat.csv',
                            usecols=[0])

    tunnusLista = tunnusDF['tunnus'].values.tolist()
    tunnusLista = sorted(tunnusLista)

apiKey = '3ab64aed-4375-4586-bfe7-fe9a7f580c03'

for tunnus in tunnusLista:
    kiTu = tunnus
    if tunnus.find('M') != -1:
        printThis = f'Kiinteistöllä {kiTu} lohkominen tms kesken, skipataan'
        print(printThis)
    else:
        printThis = f'Ladataan kiinteistön {kiTu} rajoja'
        print(printThis)
        stuff = f'PalstanSijaintitiedot/items?kiinteistotunnuksenEsitysmuoto={kiTu}'
        api = f'https://avoin-paikkatieto.maanmittauslaitos.fi/kiinteisto-avoin/simple-features/v3/collections/{stuff}'
        filename = f'./rajat/{kiTu}.json'
        r = requests.get(api, auth=(apiKey, ''))
        with open(filename, 'wb') as f:
            f.write(r.content)

print('Valmis')
