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

