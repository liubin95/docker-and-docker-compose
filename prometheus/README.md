# prometheus

## build

```shell
docker build -t liubin/prometheus .
```

## run

```shell
docker run \
    -p 9090:9090 \
    -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
    liubin/prometheus
```