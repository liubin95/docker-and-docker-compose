// Load Chance
import Chance = require('chance');
import {Kafka, Producer} from 'kafkajs';
import { Message } from './message';

class ProducerClient {
    private chance: Chance;
    private producer: Producer;
    private readonly msg_num: number;

    constructor() {
        this.msg_num = parseInt(process.argv.slice(2)[0]);
        console.log(` hello world producer ${this.msg_num}`);
        // Instantiate Chance so it can be used
        this.chance = new Chance();
        const kafka = new Kafka({
            clientId: 'node-client-producer',
            brokers: ['kafka1:9092']
        });
        this.producer = kafka.producer();
    }

    async send_msg(topic: string) {
        await this.producer.connect();
        for (let i = 0; i < this.msg_num; i++) {
            let msg = new Message(i,
                this.chance.name(),
                this.chance.age(),
                this.chance.email(),
                this.chance.city(),
                this.chance.floating({min: 100, fixed: 2}));
            console.log(`message: ${i}, ${msg}`);
            await this.producer.send({
                topic: topic,
                messages: [
                    {
                        value: msg.toString()
                    }
                ],
            });
        }
        await this.producer.disconnect();
        return "success";
    }
}

const main = new ProducerClient();
main.send_msg('test-topic').then((r) => {
    console.log(r);
}).catch((err) => {
    console.log(err);
});
