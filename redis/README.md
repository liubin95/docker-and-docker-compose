# redis

## build

### Redis replication

- [Redis 复制](https://redis.io/docs/manual/replication/)
- Redis 使用异步复制
- 一个master可以有多个replicas
- Redis 复制在主控端是非阻塞的。这意味着当一个或多个副本执行初始同步或部分重新同步时，主控将继续处理查询
- 复制既可以用于可扩展性，也可以用于只读查询的多个副本（例如，可以将缓慢的 O(N) 操作卸载到副本），或者仅用于提高数据安全性和高可用性
- 强烈建议在主服务器和副本中打开持久性。如果无法做到这一点，则应将实例配置为避免在 **自动重启**
    1. 节点 A 作为主节点，关闭持久性，节点 B 和 C 从节点 A 复制
    2. 节点 A 崩溃，重启进程，由于关闭了持久性，节点会以空数据集重新启动
    3. 节点 B 和 C 将从节点 A 复制，该节点是空的，因此它们将有效地销毁其数据副本

```shell
# config file and command
replicaof 172.18.0.2 7001
# requirepass
config set masterauth <password>
# or config file 
masterauth <password>
```

### Scaling with Redis Cluster

- [使用 Redis 集群进行扩展](https://redis.io/docs/manual/scaling/#initializing-the-cluster)
- Redis Cluster 不使用一致性散列，而是使用不同形式的分片，其中每个键在概念上都是我们所谓的散列槽的一部分。
- Redis 集群中有 16384 个哈希槽
- 单点故障

```shell
# create new cluster 
redis-cli --cluster create 172.18.0.2:7001 172.18.0.5:7001 172.18.0.8:7001
redis-cli --cluster create 172.18.0.2:7001 172.18.0.3:7001 172.18.0.4:7001 172.18.0.5:7001 172.18.0.6:7001 172.18.0.7:7001 172.18.0.8:7001 172.18.0.9:7001 172.18.0.10:7001 --cluster-replicas 2
# --cluster-replicas 1 意味着我们希望为每个创建的主服务器创建一个副本

# add new node master
redis-cli --cluster add-node 172.18.0.6:7001 172.18.0.2:7001
# add new node slave
redis-cli --cluster add-node 127.0.0.1:7006 127.0.0.1:7000 --cluster-slave --cluster-master-id <node-id>

# 新增master 节点没有hash槽，需要重新分配
# reshard
redis-cli --cluster reshard 172.18.0.6:7001
# --cluster-yes 直接yes 
redis-cli --cluster reshard 172.18.0.2:7001 --cluster-from <node-id> --cluster-to <node-id> --cluster-slots 5000 --cluster-yes

# 手动故障转移
# 在从节点上执行以下命令：
cluster failover

# delete node
# 要删除主节点，它必须为空。
redis-cli --cluster del-node 172.18.0.2:7001 <node-id>
```

## ops

### CLUSTER NODES

| node-id                                  | ip:端口                 | 标志<br/>master,slave,myself,fail, ... | 如果是副本，则为主节点 ID                           | 最后一个等待回复的 PING 的时间 | 最后一次收到 PONG 的时间 | 此节点的配置时期（请参阅集群规范） | 此节点的链接状态  | 插槽服务              |
|------------------------------------------|-----------------------|--------------------------------------|------------------------------------------|--------------------|-----------------|-------------------|-----------|-------------------|
| 7a340360c5bd160a31ca72348e4e706aadf91902 | 172.18.0.4:7001@17001 | slave                                | 03b382f29c904fc26dc8029293ee6e4c491fb48b | 0                  | 1650789342000   | 4                 | connected | -<br/>(slave没有插槽) |
| 8fd19c865f8a3fc742193592c669eb0c0818d747 | 172.18.0.2:7001@17001 | myself,slave                         | 574b4abf58f1c69d9c4b2bb417093c1f7c79d862 | 0                  | 1650789342000   | 5                 | connected | -                 |
| 574b4abf58f1c69d9c4b2bb417093c1f7c79d862 | 172.18.0.3:7001@17001 | master                               | -                                        | 0                  | 1650789341020   | 6                 | connected | 0-4999            |
| 03b382f29c904fc26dc8029293ee6e4c491fb48b | 172.18.0.6:7001@17001 | master                               | -                                        | 0                  | 1650789341522   | 4                 | connected | 5000-16383        |
| 1ee27286380ced954125decb4f76f4e09db3f220 | 172.18.0.5:7001@17001 | master                               | -                                        | 0                  | 1650789342023   | 2                 | connected | -<br/>(主节点需要重新分配) |
| 40a3303443eb14bca0db3374b43a333acce2bbe4 | 172.18.0.8:7001@17001 | master                               | -                                        | 0                  | 1650789343028   | 3                 | connected | -                 |

### maxmemory-policy 键淘汰策略

> LRU Least Recently Used的缩写，即最近最少使用</br>
> LFU Least Frequently Used的缩写，即最少使用频率</br>
> volatile 设置了过期时间的key</br>
> allkeys 所有的key</br>
> random 随机 key</br>

- noeviction **default** 对于写请求不再提供服务，直接返回错误（DEL请求和部分特殊请求除外）
- allkeys-lru
- allkeys-lfu
- allkeys-random
- volatile-lru
- volatile-lfu
- volatile-random
- volatile-ttl 设置了过期时间的key（volatile） + 剩余时间最少（ shortest remaining time-to-live (TTL)） + lfu

The policies volatile-lru, volatile-lfu, volatile-random, and volatile-ttl behave like noeviction if there are no keys to evict matching the prerequisites.</br>
如果没有key设置了过期时间 `volatile-*` 策略下 和 **default**行为一致