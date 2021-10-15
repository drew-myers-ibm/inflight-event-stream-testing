from kafka import KafkaProducer
import requests
import json
import os
import sys

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

print(limit)

producer = KafkaProducer(bootstrap_servers=bootstrap_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username=username, sasl_plain_password=password)

url = 'https://api.ibm.com/inflight/bluerun/geos/na/environments/cte/documents?sort=-received_at&limit=10'

headers = {'X-IBM-Client-Id': client_id, 'X-IBM-Client-Secret': client_secret}

r = requests.get(url, headers=headers)
inner_url = 'https://api.ibm.com/inflight/bluerun/geos/na/environments/cte/documents/'
for doc in r.json():
    doc_code = doc['documentCode']
    inner_r = requests.get(inner_url + doc_code, headers=headers)
    producer.send(topic_name, bytes(json.dumps(inner_r.json(), separators=(",", ":")), 'utf-8'))

producer.flush()
