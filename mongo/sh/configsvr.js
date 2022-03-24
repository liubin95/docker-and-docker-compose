// docker exec -it mongo.configsvr mongo
// 设置为config节点
config = {
    "_id":"replconf",
    "configsvr": true,
    "members":[
      {"_id":0,host:"mongo.configsvr:27017"}
    ]
};
rs.initiate(config);
// 查看集群状态
rs.status();