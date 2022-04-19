export class Message {
    id: Number;
    name: String;
    age: Number;
    email: String;
    city: String;
    total_price: Number;


    constructor(id: Number, name: String, age: Number, email: String, city: String, total_price: Number) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.email = email;
        this.city = city;
        this.total_price = total_price;
    }

    toString(): string {
        return JSON.stringify(this);
    }
}