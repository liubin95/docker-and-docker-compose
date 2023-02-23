# Linux

## 常用软件

- Blue man Bluetooth Manager `sudo apt install blueman`
- [vlc video player](https://www.videolan.org/vlc/download-ubuntu.html)

## cpu

### 限定任务cpu使用率

- 避免某些任务把资源消耗完
- [使用 nice、cpulimit 和 cgroups 限制 cpu 占用率](https://www.linuxidc.com/Linux/2015-01/112382.htm)

#### 临时任务

- 使用 nice 命令手动降低任务的优先级

> 下来介绍一下nice命令的使用方法，nice命令可以修改进程的优先级，这样就可以让进程运行得不那么频繁。
> 这个功能在运行cpu密集型的后台进程或批处理作业时尤为有用。
> nice值的取值范围是[-20,19],-20表示最高优先级，而19表示最低优先级。
> Linux进程的默认nice值为0。使用nice命令（不带任何参数时）可以将进程的nice值设置为10。
> 这样调度器就会将此进程视为较低优先级的进程，从而减少cpu资源的分配。

```shell
# 压缩文件时，控制cpu使用量
nice zip a.zip a.sql
# 把pid 6919 的进程优先级降低
renice +10 6919
```

#### 长久任务

- cgroups 命令集
- [Linux资源管理之cgroups简介](https://tech.meituan.com/2015/03/31/cgroups.html)

> 功能最为强大的控制组（cgroups）的用法。
> cgroups 是 Linux 内核提供的一种机制，利用它可以指定一组进程的资源分配。
> 具体来说，使用 cgroups，用户能够限定一组进程的 cpu 占用率、系统内存消耗、网络带宽，以及这几种资源的组合。
> cgroups 的优势在于它可以控制一组进程，不像前者仅能控制单进程。而 cgroups 则可以限制其他进程资源的使用。
> 就拿 CoreOS 作为例子，这是一个专为大规模服务器部署而设计的最简化的 Linux 发行版本，它的 upgrade 进程就是使用 cgroups 来管控。这样，系统在下载和安装升级版本时也不会影响到系统的性能。

```shell
sudo cgcreate -g cpu:/cpulimited
sudo cgcreate -g cpu:/lesscpulimited
```

## 内存

```shell
# show ram info
free -ht
```

|        | total | used  | free  | shared | buff/cache | available |
|--------|-------|-------|-------|--------|------------|-----------|
| Mem:   | 7.8Gi | 1.0Gi | 6.1Gi | 366Mi  | 624Mi      | 6.2Gi     |
| Swap:  | 2.0Gi | 2.0Mi | 2.0Gi |        |            |           |
| Total: | 9.8Gi | 1.0Gi | 8.1Gi |        |            |           |

```shell
# clear cache
echo 3 > /proc/sys/vm/drop_caches
```

> To free page cache:<br>
> echo 1 > /proc/sys/vm/drop_caches<br>
> To free reclaimable slab objects (includes dentries and inodes):<br>
> echo 2 > /proc/sys/vm/drop_caches<br>
> To free slab objects and page cache:<br>
> echo 3 > /proc/sys/vm/drop_caches

## 文件和文件夹

### Linux 常用 文件夹

| 文件夹        | 用途                                                                                                | 备注                            |
|------------|---------------------------------------------------------------------------------------------------|-------------------------------|
| /          | 根目录，保持越小越好，效率高，问题少                                                                                |                               |
| /bin       | 可执行文件，维护模式下可以使用的基础命令（所有用户）                                                                        | centos 已将文件移入/usr/bin。这里是链接   |
| /boot      | 开机引导。                                                                                             |                               |
| /dev       | 设备都会以文件的形式存在。/dev/sda 第一块磁盘 等等                                                                    | /dev/null 空设备                 |
| /etc       | 所有的配置文件，包括系统，和其他服务。                                                                               |                               |
| /etc/opt   | 保存opt下第三方软件的配置文件                                                                                  |                               |
| /lib       | 开机时用到的类库                                                                                          | 同/bin，已移入 /usr/lib            |
| /mnt       | 暂时挂载的设备                                                                                           |                               |
| /opt       | 第三方软件                                                                                             |                               |
| /sbin      | 可执行文件，维护模式下可以使用的基础命令（root用户）                                                                      | 同/bin，已移入 /usr/sbin           |
| /tmp       | 临时文件                                                                                              |                               |
| /usr       | 系统预设软件。因此这个目录有点类似Windows 系统的『C:\Windows\ (当中的一部份) + C:\Program files\』这两个目录的综合体                   | usr是Unix Software Resource的缩写 |
| /usr/bin   | 一般用户使用的指令                                                                                         | FHS 要求在此目录下不应该有子目录            |
| /usr/local | 自行更新的预装软件。保留原来的，新的放置此处                                                                            |                               |
| /var       | 系统运行是变动的文件。包括缓存(cache)、登录档(log file)以及某些软件运作所产生的文件， 包括程序档案(lock file, run file)，或者例如MySQL资料库的文件等等 |                               |
| /home      | 用户的home，                                                                                          | cd ~ = cd                     |
| /lib*      | /lib 不同的格式的二进位函式库，例如 /lib64 64位函数库                                                                |                               |
| /root      | root用户的home                                                                                       |                               |

> CentOS 7 在目录的编排上与过去的版本不同。比较大的差异在于将许多原本应该要在根目录(/) 里面的目录，将他内部资料全部挪到/usr 里面去，然后进行连结设定！包括底下这些：
>- /bin --> /usr/bin
>- /sbin --> /usr/sbin
>- /lib --> /usr/lib
>- /lib64 --> /usr/lib64
>- /var/lock --> /run/lock
>- /var/run --> /run

![](./image/root-dir.png)

## 磁盘

### df

> 第1列是设备名
> 第2列是磁盘总容量大小
> 第3列是已使用容量大小
> 第4列是剩余容量大小
> 第5列容量已使用百分比
> 第6列挂载点目录名称

```shell
# show disk info
[root@dev163 _data]# df -h
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                 7.8G     0  7.8G   0% /dev
tmpfs                    7.8G     0  7.8G   0% /dev/shm
tmpfs                    7.8G  9.0M  7.8G   1% /run
tmpfs                    7.8G     0  7.8G   0% /sys/fs/cgroup
/dev/mapper/centos-root   40G   40G   44K 100% /
/dev/sda1                497M  169M  328M  34% /boot
/dev/mapper/centos-data  260G   54G  206G  21% /data
overlay                  260G   54G  206G  21% /data/lib/docker/overlay2/b4262b4b82183c389399f6ab50228384d69e5e55a487b0270ec0b47e9031f59c/merged
overlay                  260G   54G  206G  21% /data/lib/docker/overlay2/da377cff0ea3ddefa38a2500b57fe01d165bfd1f99c170a53f0d425149baa6f9/merged
tmpfs                    1.6G     0  1.6G   0% /run/user/0
```

- `tmpfs`字样的是虚拟内存文件系统(此处不做展开);
- 文件系统`/dev/mapper/centos-root`的挂载点是/(根目录)，即通常所说的根分区(或根文件系统);
- `/dev/sda1`(boot分区)中保存了内核映像和一些启动时需要的辅助文件;
- `overlay`[overlay文件系统](http://dockone.io/article/1511) 一般是 docker 容器在使用;

### du

- c或--total 除了显示个别目录或文件的大小外，同时也显示所有目录或文件的总和;
- s或--summarize 仅显示总计;
- -h或--human-readable 以K，M，G为单位，提高信息的可读性;

```shell
# show dir var disk info
du -sh /var/*
# sort
du -sh /var/* | sort -rh 
```

### 挂载磁盘

```shell
# 查看磁盘挂载情况
lsblk

# 查看磁盘详情
sudo fdisk -l

# 格式化磁盘 ext4
sudo mkfs -t ext4 /dev/sdb

# 挂载
sudo mount /dev/sdb /data

# 获取磁盘的UUID
sudo blkid /dev/sdb

# 重启自动挂载
sudo vim /etc/fstab
# 要填写file system、mount point、type、options、dump、pass等六项。
# 其中mount point为我们的挂载点/data/；type为我们格式化的文件格式，ext4；options我们一般就是defaults；
# dump都是0、pass也都是0，除非挂载点是/。
UUID=38b045ea-0bcd-46dc-b5a2-76917a91d9fe /data/ ext4 defaults 0 0
```

### 链接 ln

#### 硬连接

```shell
# 创建硬连接
ln file1 file2
# 查看硬连接数
ls -l file1
# 删除硬连接
rm file2
```

##### 限制

- 不能跨分区
- 不能针对目录

#### 软连接

```shell
# 创建软连接
ln -s file1 file2
# 目录
ln -s /bin /root/bin
# 查看软连接
ls -l file2
# 删除软连接
rm file2
```

## 端口

```shell
# show port info
netstat -tunlp
# netcat
# 扫描 端口范围
nc -z -v -w2 -u 127.0.0.1 1-65535
```

## 管道符

```shell
# find string in this directory
ls | grep string
# sort dir by size desc
du -sh ./*/ |sort -rh 
# show file 10-20 lines with line number
cat -n file | sed -n '10,20p'
cat -n file | head -n 20 | tail -n 10
```

## systemctl

```shell
systemctl enable service
systemctl disable service
systemctl start service
systemctl status service -l
systemctl stop service
# show logs 
journalctl -u service
```

