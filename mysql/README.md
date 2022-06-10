# MySQL

## build

- Windows文件到容器中权限`777`，MySQL不会使用配置文件
- 简单解决：将文件设置 只读
- MySQL Docker 容器支持在启动时执行初始化脚本，脚本文件复制或挂载到MySQL docker 映像中的/docker-entrypoint-initdb.d/文件夹
- MySQL docker 容器按文件名升序从/docker-entrypoint-initdb.d/文件夹执行脚本文件 ` "./scripts/schema.sql:/docker-entrypoint-initdb.d/1.sql"`

## dev

### DDL

```sql
-- delete all data from table
TRUNCATE TABLE table_name;
```

## ops

- show mysql running processlist `show processlist;`
- kill process `kill id;`

| Id  | User | Host             | db   | Command | Time | State                           | Info                                                                                     |
|-----|------|------------------|------|---------|------|---------------------------------|------------------------------------------------------------------------------------------|
| 18  | root | 172.18.0.1:47554 | demo | Sleep   | 1940 |                                 | NULL                                                                                     |
| 22  | root | 172.18.0.1:47562 | demo | Query   | 206  | Waiting for table metadata lock | /* ApplicationName=IntelliJ IDEA 2021.3.2 */ DROP TABLE IF EXISTS tdbm_raisecapital_info |
| 27  | root | 172.18.0.1:47572 | demo | Sleep   | 1136 |                                 | NULL                                                                                     |
| 28  | root | 172.18.0.1:47574 | demo | Sleep   | 482  |                                 | NULL                                                                                     |

- show mysql uncommitted transactions `select * from information_schema.innodb_trx;`
- kill transaction `kill trx_mysql_thread_id;`

| trx\_id         | trx\_state | trx\_started        | trx\_requested\_lock\_id | trx\_wait\_started | trx\_weight | trx\_mysql\_thread\_id | trx\_query | trx\_operation\_state | trx\_tables\_in\_use | trx\_tables\_locked | trx\_lock\_structs | trx\_lock\_memory\_bytes | trx\_rows\_locked | trx\_rows\_modified | trx\_concurrency\_tickets | trx\_isolation\_level | trx\_unique\_checks | trx\_foreign\_key\_checks | trx\_last\_foreign\_key\_error | trx\_adaptive\_hash\_latched | trx\_adaptive\_hash\_timeout | trx\_is\_read\_only | trx\_autocommit\_non\_locking | trx\_schedule\_weight |
|:----------------|:-----------|:--------------------|:-------------------------|:-------------------|:------------|:-----------------------|:-----------|:----------------------|:---------------------|:--------------------|:-------------------|:-------------------------|:------------------|:--------------------|:--------------------------|:----------------------|:--------------------|:--------------------------|:-------------------------------|:-----------------------------|:-----------------------------|:--------------------|:------------------------------|:----------------------|
| 421573637730304 | RUNNING    | 2022-04-07 14:57:00 | NULL                     | NULL               | 0           | 27                     | NULL       | NULL                  | 0                    | 0                   | 0                  | 1128                     | 0                 | 0                   | 0                         | REPEATABLE READ       | 1                   | 1                         | NULL                           | 0                            | 0                            | 0                   | 0                             | NULL                  |

### data migrate

- rename

```sql
-- same instance different database
RENAME TABLE old_base.old_table TO new_base.new_table;
```

- dump

```shell
# export from old base
mysqldump -u root -p123456 -h 127.0.0.1 -P 3306 --databases old_base --tables old_table --where "id > 100" > old_table.sql
# import to new base
mysql -u root -p123456 -h 127.0.0.1 -P 3306 new_base < old_table.sql
# or into new base
use new_base;
source /old_table.sql
```