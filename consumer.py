from kafka import KafkaConsumer
import os

username = os.environ.get('IF_EVENT_USERNAME')
password = os.environ.get('IF_EVENT_PASSWORD')
bootstrap_servers = os.environ.get('IF_EVENT_BOOTSTRAP_SERVERS')
topic_name = os.environ.get('IF_EVENT_TOPIC_NAME')

consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username=username, sasl_plain_password=password)
for msg in consumer:
    print (msg)
