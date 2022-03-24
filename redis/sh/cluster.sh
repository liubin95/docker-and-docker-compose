# 创建集群
# docker exec -it redis1_1 /bin/bash
# ./Redis-trib.rb对本机名设别不了，支持的不是很好 换成ip:port的方式
redis-cli --cluster create 172.18.0.2:7001 172.18.0.5:7001 172.18.0.8:7001
# 查看集群信息
redis-cli -c -h redis1_1 -p 7001 cluster info
# 查看主从关系
redis-cli -c -h redis1_1 -p 7001 info replication