# 更多...

下面每一个方案，都经过实践证明行之有效，希望能够对你有帮助

## 域名绑定

绑定域名的前置条件是：AWX已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

AWX 域名绑定操作步骤：

1. 使用 SFTP 登录云服务器
2. 修改 [Nginx 配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值 *localhost* 修改为你的域名
   ```text
   ...
      server_name    localhost; # 改为自定义域名
   ...
   ```
3. 保存配置文件，重启[ Nginx 服务](/zh/admin-services.md#nginx)
   ```
   sudo docker pause awx_web
   ```
4. 登录AWX，依次打开：【Settings】>【System】，修改下图的 URL 地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-seturl-websoft9.png)



## 负载均衡

通过负载均衡处理多台 AWX 并行工作，对于大型企业来说这是一种很常见的部署方案。

AWX是基于Docker部署，处理web的容器名称为：awx_web

## 使用外部PostgreSQL

默认安装下，使用的是Docker版本的PostgreSQL数据库，并设置了持久化存储。  

如果你想将数据库更换为外部PostgreSQL数据库（自建或云数据库），请参考如下步骤：

1. 备份好已有的AWX数据
2. 进入到AWX的配置文件夹
   ```
   cd /data/.awx
   ```
2. 删除目前AWX项目的所有容器
   ```
   cd /data/.awx
   docker-compose -f docker-compose.yml down -v
   ```
3. 修改 *docker-compose.yml* 文件，去掉两处 *depends_on:* 项中的 *- postgres*，并删除 *postgres: ...* 整段，最后文件的内容如下： 
   ```
   version: '2'
   services:

     web:
       image: ansible/awx_web:11.2.0
       container_name: awx_web
       depends_on:
         - redis
         - memcached
       ports:
         - "80:8052"
       hostname: awxweb
       user: root
       restart: unless-stopped
       volumes:
         - supervisor-socket:/var/run/supervisor
         - rsyslog-socket:/var/run/awx-rsyslog/
         - rsyslog-config:/var/lib/awx/rsyslog/
         - "/data/.awx/SECRET_KEY:/etc/tower/SECRET_KEY"
         - "/data/.awx/environment.sh:/etc/tower/conf.d/environment.sh"
         - "/data/.awx/credentials.py:/etc/tower/conf.d/credentials.py"
         - "/data/.awx/nginx.conf:/etc/nginx/nginx.conf:ro"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 

     task:
       image: ansible/awx_task:11.2.0
       container_name: awx_task
       depends_on:
         - redis
         - memcached
         - web
       hostname: awx
       user: root
       restart: unless-stopped
       volumes:
         - supervisor-socket:/var/run/supervisor
         - rsyslog-socket:/var/run/awx-rsyslog/
         - rsyslog-config:/var/lib/awx/rsyslog/
         - "/data/.awx/SECRET_KEY:/etc/tower/SECRET_KEY"
         - "/data/.awx/environment.sh:/etc/tower/conf.d/environment.sh"
         - "/data/.awx/credentials.py:/etc/tower/conf.d/credentials.py"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
         SUPERVISOR_WEB_CONFIG_PATH: '/supervisor.conf'

     redis:
       image: redis
       container_name: awx_redis
       restart: unless-stopped
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
       command: ["/usr/local/etc/redis/redis.conf"]
       volumes:
         - "/data/.awx/redis.conf:/usr/local/etc/redis/redis.conf:ro"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"

     memcached:
       image: "memcached:alpine"
       container_name: awx_memcached
       command: ["-s", "/var/run/memcached/memcached.sock", "-a", "0666"]
       restart: unless-stopped
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
       volumes:
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"

   volumes:
     supervisor-socket:
     rsyslog-socket:
     rsyslog-config:

   ```
4. 修改 */data/.awx/credentials.py* 文件中数据库账号信息，确保为外部PostgreSQL的连接信息
   ```
      DATABASES = {
       'default': {
           'ATOMIC_REQUESTS': True,
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': "awx",
           'USER': "awx",
           'PASSWORD': "yourpassword",
           'HOST': "pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com",
           'PORT': "1433",
       }
   }

   BROADCAST_WEBSOCKET_SECRET = "al9mLS4tWTlmX1owN1FyOElJWDY="
   ```
5. 修改 */data/.awx/environment.sh* 文件中数据库账号信息，确保为外部PostgreSQL的连接信息
   ```
   DATABASE_USER=awx
   DATABASE_NAME=awx
   DATABASE_HOST=pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com
   DATABASE_PORT=1433
   DATABASE_PASSWORD=yourpassword
   AWX_ADMIN_USER=admin
   AWX_ADMIN_PASSWORD=password

   ```
6. 重新创建容器
   ```
   docker-compose -f docker-compose.yml up -d
   ```

## 额外变量

AWX 支持从项目之外注入所需的变量，它是通过**额外变量**机制实现，一方面可以增加变量的多样性，另外可以绕过 Ansible 项目中的交互式。  

有两种额外变量的方式：

* **方式一**：在【模板】编辑页面直接增加额外变量
  ![Ansible-Tower 额外变量](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-extravars-websoft9.png)

* **方式二**：在【模板】编辑页面增加一个【问卷调查】项
  ![Ansible-Tower 问卷调查](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-varspromptset-websoft9.png)

详情参考官方文档 [Create a Survey](https://docs.ansible.com/ansible-tower/latest/html/userguide/job_templates.html#ug-surveys)