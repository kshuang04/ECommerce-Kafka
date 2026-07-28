# E-Commerce Kafka Simulation
![Python Version](https://shields.io)
![Apache Kafka](https://shields.io)
![Docker](https://shields.io)

## Purpose
Just a small project to get more familiar with Kafka

## Description
This project simulates what happens purchases a product on a site.

### The Producer
The producer is a mock storefront script that outputs transaction details to an `orders` topic.

### The Consumers
The consumers are multiple independent consumer scripts reading from the same `orders` topic (to demonstrate Kafka's parallel processing).

* Consumer A: Handles inventory and updates stock counts
* Consumer B: Handles email notifications ("sends" an email receipt)
* Consumer C: Handles analytics and tracks total revenue