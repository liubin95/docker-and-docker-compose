FROM node:14.18.0
## settings timezone
ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Create app directory
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install --registry=https://registry.npm.taobao.org
# Bundle app source
COPY . .
ENTRYPOINT  ["npm","run","server"]