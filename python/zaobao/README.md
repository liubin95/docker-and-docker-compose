## build

```shell
# set env 
DINGDING_TOKEN
DINGDING_SECRET
# run build 
docker build -t python/zaobao .
```

## run

```shell
docker run -it --rm -p '8080:8080' python/zaobao
sudo docker run -d --name liubin.zaobao -p '10308:8080' -e DINGDING_TOKEN=$DINGDING_TOKEN -e DINGDING_SECRET=$DINGDING_SECRET python/zaobao
docker logs -f liubin.zaobao
```