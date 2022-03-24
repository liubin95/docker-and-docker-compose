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
- config  Validate and view the Compose file
- up  Create and start containers
  - f compose file (default: docker-compose.yml)
  - p project name (default: directory name)
- down  Stop and remove containers, networks, images, and volumes
- logs log
- https://docs.docker.com/compose/reference/
