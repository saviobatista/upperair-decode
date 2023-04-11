# Retrieves the latest TEMP for $station in JSON format using REDEMET API

import requests

station='83746'

api_key='IlWej3wrJtL1jJUczTpKIVTSuxdmWM6w1LODXOiE'
url='https://api-redemet.decea.gov.br/mensagens/temp?api_key='+api_key+'&estacao='+station
cafile='www.atd-1.com.crt'
headers={'X-Api-Key': 'IlWej3wrJtL1jJUczTpKIVTSuxdmWM6w1LODXOiE'}

temp_json = requests.get(url, headers=headers , verify=cafile).json()

ttaa_msg=temp_json['data']['data'][0]['mens']
ttbb_msg=temp_json['data']['data'][1]['mens']
ttcc_msg=temp_json['data']['data'][2]['mens']
ttdd_msg=temp_json['data']['data'][3]['mens']

print(ttaa_msg)
