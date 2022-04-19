import {Consumer, Kafka} from "kafkajs";


class ConsumerClient {
    private consumer: Consumer;

    constructor() {
        const kafka = new Kafka({
            clientId: 'node-client-producer',
            brokers: ['kafka1:9092']
        });
        this.consumer = kafka.consumer({groupId: 'node-group'})
    }

    subscribe = async (topic: string) => {
        await this.consumer.subscribe({topic: topic})
        await this.consumer.run({
            eachMessage: async ({topic, partition, message}) => {
                console.log(`Received message from ${topic}:${partition} ${message.value.toString()}`);
            }
        })
        return "done";
    };
}

const main = new ConsumerClient()
main.subscribe('test-topic').then(r => console.log(r))
