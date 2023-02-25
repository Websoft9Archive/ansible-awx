# Start or Stop the Services

These commands you must know when you using the AWX of Websoft9

## Docker Compose

```shell
#create containers
sudo docker-compose up
#re-create containers
sudo docker-compose up -d
```

## Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

### AWX

AWX have five containers: awx_task, awx_web, awx_rabbitmq, awx_postgre, awx_memcached

```shell
#AWX
sudo docker pause awx_task
sudo docker stop awx_task
sudo docker restart awx_task

#AWX-Web
sudo docker pause awx_web
sudo docker stop awx_web
sudo docker restart awx_web

#AWX-RabbitMQ
sudo docker pause awx_rabbitmq
sudo docker stop awx_rabbitmq
sudo docker restart awx_rabbitmq

#AWX-PostgreSQL
sudo docker pause awx_postgres
sudo docker stop awx_postgres
sudo docker restart awx_postgres

#AWX-Memcached
sudo docker pause awx_memcached
sudo docker stop awx_memcached
sudo docker restart awx_memcached
```