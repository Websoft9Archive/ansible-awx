# Troubleshooting

We collect the most common troubleshooting of using aaPanel for your reference:

> Many troubleshooting is closely related to the Server, if you can confirm troubleshooting is related to Cloud Platform, please refer to [Cloud Platform Documentation](https://support.websoft9.com/docs/faq/tech-instance.html)

#### Database service could not be started?

Insufficient disk space, insufficient memory, and configuration file errors can make database service could not be started  

It is recommended to first check through the command.

```shell
# restart mysql service
systemctl restart mysql

# view disk space
df -lh

# view memory rate
free -lh 
```

#### A server error has occurred?

```
docker logs awx_web
```

#### Create manful Project from SCM type have error "WARNING: There are no available playbook directories in /var/lib/awx/projects...."

Reason: The directory /var/lib/awx/projects of AWX container not mounted to Server
Solution： Mounted the container's /var/lib/awx/projects to Server's path /data/wwwroot/awx/project.

#### awx_redis container start fail?

Reason: redis.sock permission problem  
Solution:  

1. Edit file */data/.awx/redis.conf* and add the line `unixsocketperm 750`
   ```
   unixsocket /var/run/redis/redis.sock
   unixsocketperm 660
   port 0
   bind 127.0.0.1
   unixsocketperm 750
   ```
2. Set redis socket directory permission with the command `chmod -R 777 /data/.awx/redis_socket`
3. Go to AWX directory and run the container again
   ```
   cd /data/.awx
   docker-compose down -v
   docker-compose up -d
   ```

#### I can login to AWX console, but run job failed?

The  most likely reason is the **awx_redis** container can not start, you can run the command `docker ps` to check the status of  **awx_redis**

