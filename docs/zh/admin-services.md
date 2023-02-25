# 服务启停

使用由Websoft9提供的AWX部署方案，可能需要用到的服务如下：

## Docker Compose

```shell
#创建容器
sudo docker-compose up
#创建容器并重建有变化的容器
sudo docker-compose up -d
```

## Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

### AWX 容器

> 终止命令 `stop` 会从进程中释放容器的资源，但不会删除容器

```shell
#AWX-主程序
sudo docker pause awx_task
sudo docker stop awx_task
sudo docker restart awx_task

#AWX-Web界面
sudo docker pause awx_web
sudo docker stop awx_web
sudo docker restart awx_web

#RabbitMQ
sudo docker pause awx_rabbitmq
sudo docker stop awx_rabbitmq
sudo docker restart awx_rabbitmq

#PostgreSQL
sudo docker pause awx_postgres
sudo docker stop awx_postgres
sudo docker restart awx_postgres

#PostgreSQL
sudo docker pause awx_Memcached
sudo docker stop awx_Memcached
sudo docker restart awx_Memcached
```