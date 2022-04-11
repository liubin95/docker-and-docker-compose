# docker-and-docker-compose

## dicker build

```shell
# build 命令
docker build -t liubin/app .
```

## docker clean

```shell
# 删除所有停止的容器
docker rm $(docker ps -a -q)
# 删除最近10个
docker rm $(docker ps -n 10 -q)
# 删除未使用的volume
docker volume prune
```

## docker-compose

- `config`  Validate and view the Compose file
- `up`  Create and start containers
    - `-f` compose file (default: docker-compose.yml)
    - `-p` project name (default: directory name)
- `down`  Stop and remove containers, networks, images, and volumes
- `logs` [options] [SERVICE...] logs
    - `-f`   Follow log output.
    - `--tail="all"` Number of lines to show from the end of the logs for each container.
- `ps`  List containers
- `exec`  Run a command in a running container `docker-compose exec kibana sh -c "ps -aux"`
- `top`  Display the running processes of a container
- `stop`  Stop containers
- `start`  Start containers
- `restart`  Restart stopped containers
- [https://docs.docker.com/compose/reference](https://docs.docker.com/compose/reference/)