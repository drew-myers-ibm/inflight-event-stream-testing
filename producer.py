from kafka import KafkaProducer
import json
import os

username = os.environ.get('IF_EVENT_USERNAME')
password = os.environ.get('IF_EVENT_PASSWORD')
bootstrap_servers = os.environ.get('IF_EVENT_BOOTSTRAP_SERVERS')
topic_name = os.environ.get('IF_EVENT_TOPIC_NAME')

producer = KafkaProducer(bootstrap_servers=bootstrap_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username=username, sasl_plain_password=password)


directory = r'data'
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), 'rb') as reader:
        inputJson = json.loads(reader.read())
        producer.send(topic_name, bytes(json.dumps(inputJson, separators=(",", "=")), 'utf-8'))

producer.flush()
