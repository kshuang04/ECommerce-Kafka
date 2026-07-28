# E-Commerce Kafka Simulation
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)


## Purpose
Just a small project to get more familiar with Kafka

## Description
This project simulates what happens purchases a product on a site.

### The Producer
The producer (producer.py) is a mock storefront script that outputs transaction details to an `orders` topic.

### The Consumers
The consumers are multiple independent consumer scripts reading from the same `orders` topic (to demonstrate Kafka's parallel processing).

* Consumer A (inventory.py): Handles inventory, updates stock counts, and restocks inventory
* Consumer B (email.py): Handles email notifications ("sends" an email receipt)
* Consumer C (revenue.py): Handles analytics and tracks total revenue