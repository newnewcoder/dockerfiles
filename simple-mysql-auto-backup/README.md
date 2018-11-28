# How to use

please check out the [example](https://github.com/newnewcoder/dockerfiles/blob/master/simple-mysql-auto-backup/example/docker-compose.yml)

This docker image is used to automatically backup mysql DB to local storage using easy settings under `docker-compose`.
It also provides a simple web console to backup immediately, restore and delete old dump file.

![pic1](_assets/console.png)


# How to build

~~~bash
docker build -t newnewcoder/mysql-autobackup:latest . --no-cache
~~~
