# [containerd](https://github.com/containerd/containerd)

## [安装](https://github.com/containerd/containerd/blob/main/docs/getting-started.md)

```shell
yum install -y yum-utils
yum-config-manager \
  --add-repo \
  https://download.docker.com/linux/centos/docker-ce.repo
yum install -y containerd.io
systemctl start containerd
systemctl enable --now containerd

```

## [nerdctl：用于 containerd 的 Docker 兼容 CLI](https://github.com/containerd/nerdctl)

```shell
wget https://github.com/containerd/nerdctl/releases/download/v1.3.1/nerdctl-full-1.3.1-linux-amd64.tar.gz
tar -xzvf nerdctl-full-1.3.1-linux-amd64.tar.gz -C /usr/local
nerdctl run hello-world

```
