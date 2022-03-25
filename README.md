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
- https://docs.docker.com/compose/reference/

## MySQL
- Windows文件到容器中权限`777`，MySQL不会使用配置文件
- 简单解决：将文件设置 只读
## mongoDB
```shell
# 导入json 数据
mongoimport --db liubin --collection youtube_user --jsonArray /liubin_youtobe_user.json
# 导入csv
mongoimport --db liubin --collection user_behavior --type csv --fieldFile ./fieldFile.txt --numInsertionWorkers 4 ./xad.csv
```
