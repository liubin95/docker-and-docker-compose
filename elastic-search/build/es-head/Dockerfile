FROM mobz/elasticsearch-head:5
# settings  timezone
ENV TZ Asiza/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/app/_site
RUN sed -i 's:application/x-www-form-urlencoded:application/json;charset=UTF-8:g' ./vendor.js
