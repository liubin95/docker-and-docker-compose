# docker-and-docker-compose

## docker build

```shell
# build 命令
docker build -t liubin/app .
```

## docker run

```shell
# run 命令
docker run --rm -p 8080:8080 --name app -d liubin/app
```

## docker export

```shell
# export 命令
# 容器无法启动，可以导出，查看结构和log
docker export --output="app.tar" app
```

## docker clean

```shell
# 删除所有停止的容器
docker rm $(docker ps -a -q)
# 删除最近10个
docker rm $(docker ps -n 10 -q)
# 删除未使用的volume
docker volume prune
# rm unused images
docker image prune -a
# rm everything
docker system prune --volumes
```

## docker remote

### docker login

```shell
# login github packge
cat ~/pattoken.txt | docker login ghcr.io -u liubin95 --password-stdin
```

### docker tag

```shell
# tag 命令
docker tag liubin/es-head:latest ghcr.io/liubin/es-head:latest
```

### docker push

```shell
# push 命令
docker push ghcr.io/liubin/es-head:latest
```

## docker-compose

- `config`  Validate and view the Compose file
- `up`  Create and start containers
    - `-f` compose file (default: docker-compose.yml)
    - `-p` project name (default: directory name)
- `down`  Stop and remove containers, networks, images, and volumes
- `logs [options] [SERVICE...]` logs
    - `-f`   Follow log output.
    - `--tail="all"` Number of lines to show from the end of the logs for each container.
- `ps`  List containers
- `exec`  Run a command in a running container `docker-compose exec kibana sh -c "ps -aux"`
- `top`  Display the running processes of a container
- `stop`  Stop containers
- `start`  Start containers
- `restart`  Restart stopped containers
- [https://docs.docker.com/compose/reference](https://docs.docker.com/compose/reference/)