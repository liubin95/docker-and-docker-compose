# mongoDB
## build
## dev
```shell
# import json data
mongoimport --db liubin --collection youtube_user --jsonArray /liubin_youtobe_user.json
# import csv file
mongoimport --db liubin --collection user_behavior --type csv --fieldFile ./fieldFile.txt --numInsertionWorkers 4 ./xad.csv
```
