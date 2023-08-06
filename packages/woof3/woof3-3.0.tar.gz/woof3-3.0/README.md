# Woof
Persistent messaging at scale

## Introduction
Persistent messaging library which offers various flavors of messaging; optimizing for throughput, latency etc

Currently there is support for paritioned , persistent queues which use Apache Kafka as the backend. Future work will include low-latency messaging.

## Installation 

* Install requirements for woof.
```
pip3 install -r requirements.txt
```
* Install woof package
```
python3 setup.py install
```

## Sample Usage

**Producer**
```python
import sys
import os
import logging
from woof.producer import FeedProducer

fp = FeedProducer(server)
msg = "this"
fp.send(topic, " [MY MESSAGE] %s" %(msg))

```

**Keyed/Partitioned Producer**
```python
import sys
import os
import logging
from woof.partitioned_producer import PartitionedProducer

pp = PartitionedProducer(server)
pp.send(topic = topic_name, value=message_value, key=message_key)

```

**Consumer**

```python
import time, sys, logging, os
from woof.consumer import FeedConsumer

# Callback function executed for eah message.
# Arg1 - msg.key
# Arg2 - msg.value
def dummy(key, value):
    print(key + ":" + value)

fc = FeedConsumer(broker='kafka_broker_ip:kafka_broker_port',  group ='TestGroup')
fc.add_topic(topic, dummy)
fc.run()

time.sleep(60) // This is just to avoid the process exiting
```
