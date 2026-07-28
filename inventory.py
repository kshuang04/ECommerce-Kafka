import json

from confluent_kafka import Consumer

def main():
    consumer_config = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "inventory",
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(consumer_config)

    consumer.subscribe(["orders"])

    print("🟢 Consumer is running and subscribed to orders topic")

    inventory = {
        "keyboard": 20,
        "mouse": 20,
        "monitor": 10,
        "cables": 15,
        "ergonomic chair": 5,
    }

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

            # restock if not enough items to complete order
            if (inventory[order["item"]] - order["quantity"]) < 5:
                restock_quantity = order["quantity"] + 10
                inventory[order["item"]] += restock_quantity
                print(f"🔄 Restocked {restock_quantity} {order["item"]}")

            inventory[order["item"]] -= order["quantity"]

            print(f"📦 {inventory[order["item"]]} x {order["item"]} in stock")

    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer...")

    finally:
        consumer.close()

if __name__ == "__main__":
    main()
