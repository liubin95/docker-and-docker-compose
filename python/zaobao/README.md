## build

```shell
# set env 

docker build -t python/zaobao .
```

## run

```shell
docker run -it --rm -p '8080:8080' python/zaobao
docker run -d --name liubin.zaobao -p '10308:8080' python/zaobao
docker logs -f liubin.zaobao
```