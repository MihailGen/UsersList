#!/bin/bash
#Пример скрипта для создания бэкапа и восстановления системы


# Удаляем старые образы бекапы
docker rmi $(docker images | grep 'backup')

# Останавливаем текущий контейнер (если это необходимо)
docker stop user_server

# Создаём образ текущего состояния контейнера user_server
docker commit user_server user_server_backup

# Удаляем текущий контейнер (если это необходимо)
docker rm user_server

# Создаём новый контейнер из образа - бекапа
docker docker run -d -p 8000:8000 --name user_server user_server_backup