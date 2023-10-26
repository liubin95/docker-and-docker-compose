## build

```shell
# set env 
DINGDING_TOKEN
DINGDING_SECRET
# run build 
sudo docker build -t python/zaobao .
```

## run

```shell
sudo docker run -it --rm -p '8080:8080' python/zaobao

sudo docker run -d --name liubin.zaobao -p '10308:8080' \
-e DINGDING_TOKEN=$DINGDING_TOKEN \
-e DINGDING_SECRET=$DINGDING_SECRET \
-e QWEATHER_KEY=$QWEATHER_KEY \
python/zaobao

sudo docker logs -f liubin.zaobao

curl http://localhost:10308/daily -H 'authority:liubin'
```