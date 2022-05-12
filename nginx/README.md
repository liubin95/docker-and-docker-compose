# nginx

## build

```shell
docker build -t liubin/nginx .
```

## run

```shell
docker run --name nginx --rm -p 8080:80 -v $pwd/conf:/etc/nginx/conf -v $pwd/static-html-directory:/usr/share/nginx/html liubin/nginx
```

```shell
# reload nginx config
nginx -s reload
# shutdown nginx
nginx -s quit
```

