# Kafka

## build

## dev

```shell
# show topics list
kafka-topics.sh --bootstrap-server localhost:9092 --list
# show topic details
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic test-topic
# create topic
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic test-topic --partitions 3 --replication-factor 2
# delete topic
kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic test-topic
```

```shell
# produce message
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-topic
# consume message
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
# consume message with group id
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning --consumer-property group.id=test-group
```