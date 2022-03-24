// docker exec -it mongo.shard11 mongo
// 构建副本，PSA架构
config = {
    "_id":"shard2",
    "members":[
      {"_id":0,host:"mongo.shard21:27017"},
      {"_id":1,host:"mongo.shard22:27017"},
	// 仲裁节点
      {"_id":2,host:"mongo.shard23:27017","arbiterOnly":true}
    ]
};
rs.initiate(config);
// 查看集群状态
rs.status();