# elasticsearch

## build

### elasticsearch

[https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

- set **vm_max_map_count** to at least 262144
    - Linux
      ```shell
      # To apply the setting on a live system, run
      sysctl -w vm.max_map_count=262144
      # To permanently change the value for the vm.max_map_count setting
      # update the value in /etc/sysctl.conf
      # then run
      sysctl -p
      ```
    - windows wsl2
      ```shell
      wsl -d docker-desktop
      # then like Linux operating
      ```

## dev

### 关键字

- `match` search
- `terms` 精准 search
- `gt` 大于
- `lt` 小于
- `aggs` group by 分组
- [https://zq99299.github.io/note-book/elasticsearch-senior/aggs/41-query-aggs.html](https://zq99299.github.io/note-book/elasticsearch-senior/aggs/41-query-aggs.html)

## ops

# esrally

ES 官方开源的压力测试工具。基于 Python3 的 ES 压力测试命令行工具，功能丰富支持自动创建、运行、销毁 ES 集群，以及不同数据集的测试结果比较。
[文档](https://esrally.readthedocs.io/en/stable/quickstart.html)

## 基准测试

> 基准测试（benchmarking）是一种测量和评估软件性能指标的活动。
> 你可以在某个时候通过基准测试建立一个已知的性能水平（称为基准线），当系统的软硬件环境发生变化之后再进行一次基准测试以确定那些变化对性能的影响。
> 这是基准测试最常见的用途。其他用途包括测定某种负载水平下的性能极限、管理系统或环境的变化、发现可能导致性能问题的条件，等等。

相同数据在不同硬件下的测试结果。来确定当前集群性能

## install

```shell
docker pull elastic/rally
# 可供测试的场景数据
docker run elastic/rally list tracks
```

## Tracks

您可以为基准选择不同的基准情景（称为Tracks）

```shell
# 测试已经存在的集群
docker run elastic/rally esrally race \
# 数据场景
 --track=pmc \
 # 地址
 --target-hosts=172.16.20.141:9200,172.16.20.176:9200,172.16.20.184:9200 \
 # --pipeline=benchmark-only Rally 不为我们配置集群。
 --pipeline=benchmark-only
```


