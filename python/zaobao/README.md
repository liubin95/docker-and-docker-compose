## build

```shell
docker build -t python/zaobao .
```

## run

```shell
docker run -it --rm -p '8080:8080' python/zaobao
docker run -d --name liubin.zaobao -p '8080:8080' python/zaobao
```