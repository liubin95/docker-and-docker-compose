FROM bitnami/kafka:3.1

## settings timezone
ENV TZ Asia/Shanghai
USER root
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone