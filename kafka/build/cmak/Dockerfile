FROM openjdk:11.0

## settings timezone
ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY cmak/ /opt/cmak/
WORKDIR /opt/cmak
CMD ["./bin/cmak","-Dcmak.zkhosts=zook:2181"]