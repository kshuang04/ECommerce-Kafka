import json

from confluent_kafka import Consumer

def main():
    consumer_config = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "revenue",
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(consumer_config)

    consumer.subscribe(["orders"])

    print("🟢 Consumer is running and subscribed to orders topic")

    prices = {
        "keyboard": 12.99,
        "mouse": 9.99,
        "monitor": 99.99,
        "cables": 5.99,
        "ergonomic chair": 149.99,
    }

    total_revenue = 0

    try:
        while True:
            msg = consumer.poll()
            if msg is None:
                continue
            if msg.error():
                print(f"❌ Error: {msg.error()}")
                continue

            value = msg.value().decode("utf-8")
            order = json.loads(value)

            total_revenue += order["quantity"] * prices[order["item"]]

            print(f"💰 Total revenue: ${total_revenue:.2f}")

    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer...")

    finally:
        consumer.close()

if __name__ == "__main__":
    main()
