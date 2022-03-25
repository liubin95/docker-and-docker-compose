# 查看集群状态
docker exec zoo3 bash -c "zkServer.sh status"
# 操作
create /zk_test my_data
get /zk_test
get /zk_test my_data1