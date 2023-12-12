# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

ENV DINGDING_SECRET=$DINGDING_SECRET
ENV DINGDING_TOKEN=$DINGDING_TOKEN
ENV QWEATHER_KEY=$QWEATHER_KEY

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# tsinghua
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app

# Creates a non-root user and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["python", "main.py"]
CMD ["uvicorn" ,"main:app","--host", "127.0.0.1", "--port", "8080"]
