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

> 功能最为强大地控制组（cgroups）的用法。
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

## 正则和文件处理

### 正则表达式

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

## shell /bash

### 种类

- Bourne Shell（/usr/bin/sh或/bin/sh）
- Bourne Again Shell（/bin/bash） 是Linux 预设的shell
- C Shell（/usr/bin/csh）
- Korn Shell（/usr/bin/ksh）
- Shell for Root（/sbin/sh）
- POSIX Shell（/bin/sh）
- Z Shell（/bin/zsh）macOS 预设的shell
- ……

### 变量

- 变量名和等号之间不能有空格

#### 变量名

- 变量名只能使用英文字母，数字和下划线，首个字符不能以数字开头
- 不能使用标点符号
- 不能使用bash里的关键字（可用help命令查看保留关键字）
- 不能使用空格赋值，变量名=变量值
- 变量名区分大小写
- 读取变量值时，变量名前面加美元符号$，如：$name
- 变量名外面的花括号是可选的，加不加都行，如：${name}或$name
- 变量名如果是复合形式，如：${name}1，花括号是必须的，如：${name}1

#### 变量值

- 变量值可以是数字、字母、字符串、特殊字符等
- 变量值可以为空。删除变量 `unset name`
- 变量值如果是复合形式，如：$name1，变量值要用双引号括起来，如："$name"1
- 变量值如果包含空格，必须用双引号括起来，如：name="my name is tom"
- 除了让**变量不解析**使用单引号，其他情况都可以使用双引号。
- 反单引号『`指令`』或 『$(指令)』
- 追加变量内容 `PATH=${PATH}:/home/bin`
- 若该变量需要在其他子程序执行，需要以export 来使变量变成环境变量

```shell
# 变量赋值
name="tom"
# 变量引用
echo $name
# 变量删除
unset name
# 空格
name="my name is tom"
# 复合形式
home="$name at home"
home="${name} at home"
# 特殊字符
name='this is a $name' # $name 不会被解析
# 双引号
name="this is a \"name\""
# 单引号
name="this is a 'name'"
# 指令
name=`date`
name=$(date)
```

#### 环境变量

> 为什么需要环境变量?</br>
> 当你登入Linux 并取得一个bash 之后，你的bash 就是一个独立的程序，这个程序的识别使用的是一个称为程序识别码，被称为PID 的就是。接下来你在这个bash 底下所下达的任何指令都是由这个bash 所衍生出来的，那些被下达的指令就被称为子程序了。</br>
> 我们在原本的bash 底下执行另一个bash ，结果操作的环境介面会跑到第二个bash 去(就是子程序)， 那原本的bash 就会在暂停的情况(睡着了，就是sleep)。整个指令运作的环境是实线的部分！若要回到原本的bash 去， 就只有将第二个bash 结束掉(下达exit 或logout) 才行。</br>
> **子程序仅会继承父程序的环境变量， 子程序不会继承父程序的自订变量啦**

![](./image/shell-1.png)

- 环境变量是系统中所有用户都能访问的变量
- 环境变量一般大写
- 分享自己的变量设定给后来呼叫的档案或其他程序

```shell
# 查看环境变量
env
# 查看某个环境变量
echo $PATH
# 设置环境变量
export PATH=/home/bin:$PATH
# 删除环境变量
unset PATH
# 变量导出
export PATH
```

### 常用命令

- `echo` 显示字符串
- `read` 读取键盘输入

```shell
read -p "请输入用户名：" name
echo "你输入的用户名是：$name"
```

- `declare / typeset` 声明变量类型

```shell
# -r 只读
# -i 整数
# -a 数组
# -x 导出
declare -r name="tom"
declare -i age=18+18 # age=36
age=18+18 # age=18+18
declare -a arr=(1 2 3)
echo ${arr[0]} # 1
declare -x name="tom"
```

- `alias` 缩写

```shell
alias ll='ls -l --color=auto'
unalias ll
```

- `history` 查看历史命令

```shell
# 查看历史命令
history
# 查看历史命令并执行
!n
# 执行上一个指令
!!
# 执行上一个以xxx开头的指令
!xxx
```

- `test` 测试条件
- `expr` 运算
- `source` 读取并执行文件内容

```shell
source ~/.bashrc
. ~/.bashrc
```

### 资源限制 ulimit

```shell
# 查看资源限制
ulimit -a
# 设置资源限制
ulimit -c 1024 # core文件大小
ulimit -d 1024 # 数据段大小
ulimit -f 1024 # 文件大小
ulimit -m 1024 # 内存大小 **
ulimit -n 1024 # 打开文件数
ulimit -s 1024 # 栈大小
ulimit -t 1024 # cpu时间 **
ulimit -u 1024 # 进程数 **
ulimit -v 1024 # 虚拟内存
ulimit -x 1024 # 文件锁定数
# -S ：soft limit ，警告的设定，可以超过这个设定值，但是若超过则有警告讯息。
# -H ：hard limit ，严格的设定，必定不能超过这个设定的数值；
```

### 特殊字符

- `~` 用户主目录
- `.` 当前目录
- `..` 上级目录
- `*` 通配符 代表『 0 个到无穷多个』任意字元
- `?` 通配符 代表『一定有一个』任意字元
- `[]` 通配符 同样代表『一定有一个在括号内』的字元(非任意字元)。例如[abcd] 代表『一定有一个字元， 可能是a, b, c, d 这四个任何一个』
- `[-]` 通配符 代表『一定有一个在括号内』的字元(非任意字元)。例如[a-d] 代表『一定有一个字元， 可能是a, b, c, d 这四个任何一个』
- `[^]` 通配符 代表『一定有一个不在括号内』的字元(非任意字元)。例如[^a-d] 代表『一定有一个字元， 可能是a, b, c, d 以外的任何一个』
- `|` 管道
- `>` 重定向
- `>>` 追加重定向
- `&` 后台执行
- `#` 注释
- `\\` 转义字符
- `;` 连续指令下达分隔符号：连续性命令的界定(注意！与管线命令并不相同)
- `()` 子程序
- `{}` 组合命令

### 重定向 > >>

> 标准输出指的是『指令执行所回传的正确的讯息』standard output (简称stdout)，而标准错误输出可理解为『 指令执行失败后，所回传的错误讯息』standard error output (简称stderr) 。

1. 标准输入 stdin 代码为 0
2. 标准输出 stdout 代码为 1
3. 标准错误输出 stderr 代码为 2

```shell
# 重定向
ll > test.txt
# 追加重定向
ll >> test.txt
# 重定向错误输出
ll 2> test.txt
# 重定向标准输出和错误输出
ll -123 > ll 2> err
# 丢弃标准输出
ll > /dev/null
# 丢弃标准错误输出
ll 2> /dev/null
# 同一个文件
ll > test.txt 2>&1
ll &> test.txt
```

```shell
# 读取键盘输入
cat > test.txt
# 文件作为输入 
cat > catfile < test.txt
# eof
cat > catfile << eof
> 123
> 456
> eof
```

### 多命令执行

#### cmd;cmd

```shell
# 顺序执行
sync; sync; shutdown -h now
```

#### && ||

```shell
# && 前面的命令执行成功后才执行后面的命令
cd /home && ls
# || 前面的命令执行失败后才执行后面的命令
cd /notexit || ls
# 判断目录是否存在，不存在则创建，然后创建文件
cd /home/test || mkdir -p /home/test && touch /home/test/test.txt
```

### 管道 pipe

```shell
# find string in this directory
ls | grep string
# 排除空行
grep -v '^$' filename
# sort dir by size desc
du -sh ./*/ |sort -rh 
# show file 10-20 lines with line number
cat -n file | sed -n '10,20p'
cat -n file | head -n 20 | tail -n 10
```

#### cut

```shell
# cut -d 分隔符 -f 列数
echo $PATH | cut -d ':' -f 1,2
# cut -c 字符位置
echo $PATH | cut -c 1-5
```

#### sort

```shell
# sort -r 逆序
# sort -n 数字排序
# sort -k 列数
# sort -t 分隔符
# sort -u 去重
# sort -b 忽略前导空格
# sort -f 忽略大小写

tail -n 10 /etc/passwd | cut -d ':' -f 1,2,3  | sort -t ':' -k 3 -n -r
```

#### uniq

```shell
# uniq -c 统计重复行数
# uniq -i 忽略大小写
last | cut -d ' ' -f1 | sort | uniq -c
```

#### wc

```shell
# wc -l 行数
# wc -w 单词数
# wc -c 字符数
wc index.zsh
cat /etc/man_db.conf | wc
# 输出的三个数字中，分别代表： 『行、字数、字元数』
```

#### tee

```shell
# tee -a 追加
# tee 会同时将资料流分送到档案去与萤幕(screen)；而输出到萤幕的，其实就是stdout ，那就可以让下个指令继续处理喔！
last | tee last.list | cut -d " " -f 1 
```

#### 文字处理

- `tr` 转换或删除字符
- `join` 将两个已排序的文件按照相同的字段进行合并。**在使用join 之前，你所需要处理的档案应该要事先经过排序(sort) 处理**

```shell
# 选项与参数：
# -t ：join 预设以空白字元分隔资料，并且比对『第一个栏位』的资料，
#       如果两个档案相同，则将两笔资料联成一行，且第一个栏位放在第一个！
# -i ：忽略大小写的差异；
# -1 ：这个是数字的1 ，代表『第一个档案要用那个栏位来分析』的意思；
# -2 ：代表『第二个档案要用那个栏位来分析』的意思。
join -t ':' -1 4  -2 3 /etc/passwd /etc/group | tail -n 10
```

- `paste` 将多个文件的内容按行合并 将两行贴在一起，且中间以[tab] 键隔开
- `expand` 将制表符转换为空格
- `unexpand` 将空格转换为制表符
- `split` 将文件分割成多个小文件

```shell
# split [OPTION]... [INPUT [PREFIX]]
# 选项与参数：
# -b ：指定每个小文件的大小，单位为『块』；
# -l ：指定每个小文件的大小，单位为『行』；
split -b 300k /etc/services services # 按照300k分割
split -l 100 /etc/services services # 按照100行分割
# 合并
cat services* > /etc/services
# 使用ls -al / 输出的资讯中，每十行记录成一个档案
ls -al / | split -l 10 - ll
```

- `xargs` 将命令的输出结果作为参数传递给另一个命令

```shell
# 很多指令其实并不支援管线命令，因此我们可以透过xargs 来提供该指令引用standard input 之用！
# 选项与参数：
# -n ：指定每次传递给命令的参数个数；
# -d ：指定分隔符，默认是以『空白字元』作为分隔符；
# -p ：指定命令执行前的提示信息；
# 删除test开头的文件
ls | grep test | xargs rm -f
```

- `-` 代表标准输入

```shell
# 管道命令中代替 filename
ls -al / | split -l 10 - ll
```

### 编写shell

```shell
#!/bin/bash

```