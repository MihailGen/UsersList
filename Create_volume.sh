#!/bin/bash
#Пример скрипта для создания независимого volume с данными

docker volume create user_data:/var/lib/postgresql/data

docker run --rm -v user_data:/var/lib/postgresql/data -v /backup:/backup busybox cp -a /backup/. /var/lib/postgresql/data