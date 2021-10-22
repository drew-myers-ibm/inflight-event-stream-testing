from kafka import KafkaProducer
import requests
import json
import os
import sys

geo = 'na'
environment = 'cte'
customer = 'scbn-trial-buyer'
base_url = 'https://api.ibm.com/inflight/bluerun/geos/' + geo + '/environments/' + environment

client_id = os.environ.get('IF_API_KEY_ID')
client_secret = os.environ.get('IF_API_KEY_SECRET')

username = os.environ.get('IF_EVENT_USERNAME')
password = os.environ.get('IF_EVENT_PASSWORD')
bootstrap_servers = os.environ.get('IF_EVENT_BOOTSTRAP_SERVERS')
topic_name = os.environ.get('IF_EVENT_TOPIC_NAME')

args = sys.argv[1:]
if not args:
    limit = 10
else:
    limit = int(args[0])

producer = KafkaProducer(bootstrap_servers=bootstrap_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username=username, sasl_plain_password=password)

url = base_url + '/documents?sort=-received_at&limit=' + str(limit)

headers = {'X-IBM-Client-Id': client_id, 'X-IBM-Client-Secret': client_secret}

r = requests.get(url, headers=headers)
inner_url = base_url + '/documents/'
for doc in r.json():
    doc_code = doc['documentCode']
    inner_r = requests.get(inner_url + doc_code, headers=headers)
    detailed_doc = inner_r.json()
    detailed_doc['geo'] = geo
    detailed_doc['environment'] = environment
    detailed_doc['companyId'] = customer
    producer.send(topic_name, bytes(json.dumps(detailed_doc, separators=(",", ":")), 'utf-8'))

producer.flush()
