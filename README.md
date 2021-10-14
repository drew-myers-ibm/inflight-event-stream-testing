# inflight-event-stream-testing

Test script for driving InFlight Document traffic onto Kafka topic.

### Setup
Install [kafka-python](https://github.com/dpkp/kafka-python)

Set the following environment variables with the appropriate values:
```
IF_EVENT_USERNAME
IF_EVENT_PASSWORD
IF_EVENT_BOOTSTRAP_SERVERS
IF_EVENT_TOPIC_NAME
```

### Usage
Run `producer.py`

The script will pick up every file in the `data` directory and put it onto the configured kafka topic.
If you want to send new or different data, just drop json files into the `data` directory.

If you have need to consume messages from the topic you can use the `consumer.py` script, which is configured the same way as the producer.
