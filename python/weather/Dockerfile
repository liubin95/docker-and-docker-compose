FROM python:3.8
RUN pip install --upgrade pip
# 安装依赖
COPY requirements.txt /tmp/requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /tmp/requirements.txt
# 复制代码
COPY .. /app
WORKDIR /app
# 启动
CMD ["uvicorn" ,"main:app","--host", "0.0.0.0"]
