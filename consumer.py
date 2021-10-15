from kafka import KafkaConsumer
import os
import requests
import json

client_id = os.environ.get('IF_API_KEY_ID')
client_secret = os.environ.get('IF_API_KEY_SECRET')

username = os.environ.get('IF_EVENT_USERNAME')
password = os.environ.get('IF_EVENT_PASSWORD')
bootstrap_servers = os.environ.get('IF_EVENT_BOOTSTRAP_SERVERS')
topic_name = os.environ.get('IF_EVENT_TOPIC_NAME')

consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username=username, sasl_plain_password=password)

url = 'https://api.ibm.com/inflight/bluerun/geos/na/environments/cte/payloads/'

headers = {'X-IBM-Client-Id': client_id, 'X-IBM-Client-Secret': client_secret}

for msg in consumer:
    event = json.loads(msg.value)
    for id in event['process']['ids']:
        file_guid = event['process']['events'][id]['file']['guid']
        r = requests.get(url + file_guid, headers=headers)
        print(r.text)
