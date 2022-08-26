# Linux

## ram

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

## disk

```shell
# show disk info
df -h
# show dir var disk info
du -sh /var/*
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

## port

```shell
# show port info
netstat -tunlp
# netcat
# 扫描 端口范围
nc -z -v -w2 -u 127.0.0.1 1-65535
```

## pipeline

```shell
# find string in this directory
ls | grep string
# sort dir by size desc
du -sh ./*/ |sort -rh 
```

# systemctl 

```shell
systemctl enable service
systemctl disable service
systemctl start service
systemctl status service -l
systemctl stop service
# show logs 
journalctl -u service
```

