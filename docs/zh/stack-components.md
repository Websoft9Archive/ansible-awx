# 参数

AWX 预装包包含 AWX 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

## 路径

本项目基于Docker安装，下面主要列出Docker有关的参数：

### Docker Container

通过运行`docker ps`，可以查看到AWX运行时所有的Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
e240ed8209cd        awx_task:1.0.0.8    "/tini -- /bin/sh ..."   2 minutes ago       Up About a minute   8052/tcp                             awx_task
1cfd02601690        awx_web:1.0.0.8     "/tini -- /bin/sh ..."   2 minutes ago       Up About a minute   0.0.0.0:443->8052/tcp                 awx_web
55a552142bcd        memcached:alpine    "docker-entrypoint..."   2 minutes ago       Up 2 minutes        11211/tcp                            memcached
84011c072aad        rabbitmq:3          "docker-entrypoint..."   2 minutes ago       Up 2 minutes        4369/tcp, 5671-5672/tcp, 25672/tcp   rabbitmq
97e196120ab3        postgres:9.6        "docker-entrypoint..."   2 minutes ago       Up 2 minutes        5432/tcp                             postgres
```

### Docker Volume

使用 *sudo docker volume ls* 查询所有 volumes，其中：

awx_postgres 挂载的目录：*/var/lib/postgresql/data*  
awx_rabbitmq 挂载的目录：*/var/lib/rabbitmq*  
awx_web 挂载的目录：*/var/lib/nginx*   
awx_task 挂载的目录：*/var/lib/nginx* 	


### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker 存储卷：*/var/lib/docker/volumes*  
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建

### Docker Compose

本环境使用 Docker Compose 作为容器编排（调度）工具，用于管理多个容器的启动和服务连接。

Docker Compose 命令位置：*/usr/local/bin/docker-compose*  
Docker Compose 配置目录 */data/.awx*  

### PostgreSQL

PostgreSQL 数据持久存储：*/data/pgdocker*

## 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| PostgreSQL | 5432 | TCP访问PostgreSQL | Optional |
| PgAdmin | 9090 | 可视化访问PostgreSQL | Optional |
| HTTP | 80 | 通过http访问AWX | 必须 |
| HTTPS | 443 | 通过https访问AWX | 可选 |

## 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

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
