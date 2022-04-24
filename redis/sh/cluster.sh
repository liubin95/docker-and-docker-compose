# 创建集群
# docker exec -it redis1_1 /bin/bash
# docker exec -it redis1_1 redis-cli -c -h redis1_1 -p 7001
# ./Redis-trib.rb对本机名设别不了，支持的不是很好 换成ip:port的方式
redis-cli --cluster create 172.18.0.2:7001 172.18.0.5:7001 172.18.0.8:7001
# 查看集群信息
redis-cli -c -h redis1_1 -p 7001 cluster info
# 查看节点
redis-cli -c -h redis1_1 -p 7001 cluster nodes
# 节点 加副本
redis-cli --cluster add-node 172.18.0.9:7001 172.18.0.2:7001 --cluster-slave --cluster-master-id 03b382f29c904fc26dc8029293ee6e4c491fb48b
redis-cli --cluster add-node 172.18.0.10:7001 172.18.0.2:7001 --cluster-slave --cluster-master-id 03b382f29c904fc26dc8029293ee6e4c491fb48b

# 查看主从关系
redis-cli -c -h redis1_1 -p 7001 info replication