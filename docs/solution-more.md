# More

Each of the following solutions has been proven to be effective and We hope to be helpful to you.

## Domain binding

The precondition for binding a domain is that AWX can accessed by domain name.

Nonetheless, from the perspective of server security and subsequent maintenance considerations, the **Domain Binding** step cannot be omitted.

AWX domain name binding steps:

1. Use **SFTP** to connect your Cloud Server
2. Modify [Nginx configuration file](/stack-components.md#nginx), change the **server_name**'s value *localhost* to your domain name
   ```text
   ...
      server_name    localhost; # Change to a your domain name
   ...
   ```
3. Save it and restart [Nginx Service](/admin-services.md#nginx)
   ```
   sudo docker restart nginx
   ```
## High availability

Processing multiple AWXs in parallel through load balancing is a very common deployment solution for large enterprises.

AWX is based on Docker deployment, the name of the container that handles the web is: awx_web


## Use an external PostgreSQL

AWX requires access to a PostgreSQL database, and by default, one will be created and deployed in a container, and data will be persisted to a host volume. In this scenario, Websoft9's deployment have set the value of postgres_data_dir to a path that can be mounted to the container. When the container is stopped, the database files will still exist in the specified path.

If you wish to use an external database (e.g [posgtresql](https://github.com/ansible/awx/blob/devel/INSTALL.md#docker-compose) ), following is the steps:

1. Backup all your data of AWX
2. Use SFTP to connect you AWX server and cd to AWS configure folder
   ```
   cd /data/.awx
   ```
2. Delete all dockers
   ```
   docker-compose -f docker-compose.yml down -v
   ```
3. Remove all **postgres** related items in the file *docker-compose.yml*  

   * Remove *- postgres* on the *depends_on:* 
   * Remove all paragraph of *postgres: ...*

   The following is the example after remove all **postgres** related items of docker-compose.yml

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
4. Modify the file */data/.awx/credentials.py* , make sure it is the correct connections for your external PostgreSQL
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
5. Modify the file */data/.awx/environment.sh* , make sure it is the correct connections for your external PostgreSQL
   ```
   DATABASE_USER=awx
   DATABASE_NAME=awx
   DATABASE_HOST=pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com
   DATABASE_PORT=1433
   DATABASE_PASSWORD=yourpassword
   AWX_ADMIN_USER=admin
   AWX_ADMIN_PASSWORD=password

   ```
6. Restart all dockers
   ```
   docker-compose -f docker-compose.yml up -d
   ```
   
## Use an external PostgreSQL with SSL mode

Assume that you have complete the **Use an external PostgreSQL** successfully, then if you want to enable the SSL mode of PostgreSQL, just need to modify the followng files

1. /data/.awx/credentials.py

```
DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres",
        'USER': "postgres@w9postgres",
        'PASSWORD': "Qwer1234",
        'HOST': "w9postgres.postgres.database.azure.com",
        'PORT': "5432",
        'SSLMODE': "require",
    }
}

BROADCAST_WEBSOCKET_SECRET = "alJ5ckRvUW9ISnpidVouWGxxNG8="
```
2. /data/.awx/environment.sh
```
DATABASE_USER=postgres@w9postgres
DATABASE_NAME=postgres
DATABASE_HOST=w9postgres.postgres.database.azure.com
DATABASE_PORT=5432
DATABASE_PASSWORD=Qwer1234
AWX_ADMIN_USER=admin
DATABASE_SSLMODE: prefer
AWX_ADMIN_PASSWORD=password

```

## Extra variable

AWX support variable outside the Ansible project, it is **Extra variable** which can help you to pass **var_promots**  

There are two ways of additional variables:

* **Method one**: Add additional variables directly on the 【template】 page
  ![Ansible-Tower Add additional variables](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-extravars-websoft9.png)

* **Method two**: Edit 【EDIT SURVEY】 link directly on the 【template】 page
  ![Ansible-Tower EDIT SURVEY](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-varspromptset-websoft9.png)

More details please refer to official docs: [Create a Survey](https://docs.ansible.com/ansible-tower/latest/html/userguide/job_templates.html#ug-surveys)