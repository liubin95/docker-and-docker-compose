# mongoDB

## build

```js
// show collections index
db.book.getIndexes();
// create index
db.book.ensureIndex({title: 1, auth: -1}, {
    name: "title_auth_index",
    unique: true,
    background: true,
});
// drop index
db.book.dropIndex("title_auth_index");
```

- keys，要建立索引的参数列表。如：{KEY:1}，其中key表示字段名，1表示升序排序，也可使用使用数字-1降序。
- options，可选参数，表示建立索引的设置。可选值如下：
  - background，Boolean，在后台建立索引，以便建立索引时不阻止其他数据库活动。默认值 false。
  - unique，Boolean，创建唯一索引。默认值 false。
  - name，String，指定索引的名称。如果未指定，MongoDB会生成一个索引字段的名称和排序顺序串联。
  - dropDups，Boolean，创建唯一索引时，如果出现重复删除后续出现的相同索引，只保留第一个。
  - sparse，Boolean，对文档中不存在的字段数据不启用索引。默认值是 false。
  - v，index version，索引的版本号。
  - weights，document，索引权重值，数值在 1 到 99,999 之间，表示该索引相对于其他索引字段的得分权重

## dev

### data

```shell
# export data
mongoexport -d mongo -c book -o book.json
```

```shell
# import json data
mongoimport --db liubin --collection youtube_user --jsonArray /liubin_youtobe_user.json
# import csv file
mongoimport --db liubin --collection user_behavior --type csv --fieldFile ./fieldFile.txt --numInsertionWorkers 4 ./xad.csv
```

### query

```js
// group by user_id 
// select user_id, count(*) as count from user_behavior group by user_id
db.user_behavior.aggregate([
                             {$group: {_id: "$user_id", count: {$sum: 1}}},
                             {$sort: {count: -1}},
                             {$limit: 10},
                           ]);
```
