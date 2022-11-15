// docker exec -it mongo.mongos mongo
sh.addShard("shard1/mongo.shard11:27017,mongo.shard12:27017,mongo.shard13:27017");
sh.addShard("shard2/mongo.shard21:27017,mongo.shard22:27017,mongo.shard23:27017");
// 查看分片状态
sh.status();
// creat database
"use liubin";
// 开启分片(数据库)
sh.enableSharding("liubin");
db.createCollection("book");
// 设置分片键
sh.shardCollection("liubin.book", { bookId: "hashed" }, false, { numInitialChunks: 2 });
// 查看文档数量
db.book.find().count();
// 查看分片状态
db.book.getShardDistribution();