# Parameters

The AWX deployment package contains a sequence software (referred to as "components") required for AWX to run. The important information such as the component name, installation directory path, configuration file path, port, version, etc. are listed below.

Use **SSH** to connect Server and run the command `docker ps`, you can list all containers that need for AWX: 

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
e240ed8209cd        awx_task:1.0.0.8    "/tini -- /bin/sh ..."   2 minutes ago       Up About a minute   8052/tcp                             awx_task
1cfd02601690        awx_web:1.0.0.8     "/tini -- /bin/sh ..."   2 minutes ago       Up About a minute   0.0.0.0:443->8052/tcp                 awx_web
55a552142bcd        memcached:alpine    "docker-entrypoint..."   2 minutes ago       Up 2 minutes        11211/tcp                            memcached
84011c072aad        rabbitmq:3          "docker-entrypoint..."   2 minutes ago       Up 2 minutes        4369/tcp, 5671-5672/tcp, 25672/tcp   rabbitmq
97e196120ab3        postgres:9.6        "docker-entrypoint..."   2 minutes ago       Up 2 minutes        5432/tcp                             postgres
```

## Path

### Docker storage

Run the command `sudo docker volume ls` to list all volumes: 

awx_postgres volume mount: */var/lib/postgresql/data*  
awx_rabbitmq volume mount: */var/lib/rabbitmq*  
awx_web volume mount: */var/lib/nginx*   
awx_task volume mount: */var/lib/nginx* 	

### Docker

Docker root directory: */var/lib/docker*  
Docker image directory: */var/lib/docker/image*   
Docker volumes: */var/lib/docker/volumes*  
Docker daemon.json: you should create this file in the directory of */etc/docker* by yourself

### Docker Compose

This environment uses Docker Compose as a container orchestration (scheduling) tool for managing multiple container configurations, launches, and service connections.

Docker Compose configuration file */usr/local/bin/docker-compose*  
Docker Compose command directory */data/awx/awxcompose*  

### PostgreSQL

PostgreSQL data storage: */data/pgdocker*

## Ports

These Ports is need when use AWX, refer to [Safe Group Setting on Cloud Console](https://support.websoft9.com/docs/faq/tech-instance.html)

| Name | Number | Use |  Necessity |
| --- | --- | --- | --- |
| PostgreSQL | 5432 | Remote connect PostgreSQL | Optional |
| PgAdmin | 9090 | CGI of PostgreSQL | Optional |
| HTTP | 80 | HTTP requests for AWX | Required |
| HTTPS | 443 | HTTPS requests AWX | Optional |

## Version

You can see the version from product page of Marketplace. However, after being deployed to your server, the components will be automatically updated, resulting in a certain change in the version number. Therefore, the exact version number should be viewed by running the command on the server:

```shell
# Linux Version
lsb_release -a

# Python Version
python --version

# Docker Version
docker -v

# Docker image lists(includes version)
sudo docker images

# Docker Compose Version
docker-compose --version
```
