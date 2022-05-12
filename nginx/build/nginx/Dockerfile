FROM nginx:1.20-alpine

# settings timezone
ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#COPY ./nginx.conf /etc/nginx/nginx.conf
#COPY ./static-html-directory /usr/share/nginx/html
CMD ["nginx", "-c", "/etc/nginx/conf/nginx.conf","-g daemon off;"]