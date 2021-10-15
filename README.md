# inflight-event-stream-testing

Test script for driving InFlight Document traffic onto Kafka topic and consuming data from that topic.

### Setup
Install [kafka-python](https://github.com/dpkp/kafka-python)
Install [requests](https://docs.python-requests.org/en/latest/user/install/#install)

Set the following environment variables with the appropriate values:
```
IF_EVENT_USERNAME
IF_EVENT_PASSWORD
IF_EVENT_BOOTSTRAP_SERVERS
IF_EVENT_TOPIC_NAME
IF_API_KEY_ID
IF_API_KEY_SECRET
```

### Usage
The `producer.py` script will pull the most recent data from the InFlight tracking data REST API and put it onto the configured kafka topic. By default it will pull the 10 most recent documents, that number can be changed by passing a number as an argument to the script.

The `consumer.py` script consumes tracking events from the configured topic, grabs the payload IDs from the process events and then retrieves the payloads using the read Payload API and prints them.

If using both together, start the consumer before the producer as the consumer starts at the latest offset and ingores messages from before it started.
