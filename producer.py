import json
import random
import time
import uuid

from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092",
}

producer = Producer(producer_config)

def transaction_report(err, msg):
    if err:
        print(f"❌ Transaction failed: {err}")
    else:
        print(f"✅ Transaction sent to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

def generate_order():
    items = ["keyboard", "mouse", "monitor", "cables", "ergonomic chair"]
    users = ["alice", "bob", "charlie", "david"]

    return {
        "order_id": str(uuid.uuid4()),
        "item": random.choice(items),
        "quantity": random.randint(1, 10),
        "user": random.choice(users),
    }

try:
    while True:
        order = generate_order()
        value = json.dumps(order).encode("utf-8")

        producer.produce(
            topic="orders",
            value=value,
            callback=transaction_report
        )

        producer.poll(0)

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🔴 Stopping producer...")

finally:
    producer.flush()