# 故障处理

此处收集使用 AWX 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 已经通过AWX安装了环境的受控端主机，更换镜像后，再次连接会报错？

找到主机缓存文件：*/var/lib/awx/.ssh/known_hosts*，删除其中的历史记录即可

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### 登录界面显示"is updating"？

等待更新完成后，重启服务器，再访问

#### 创建项目选择手动（SCM 类型）提示 "WARNING: There are no available playbook directories in /var/lib/awx/projects...."？

原因：AWX容器的项目路径没有挂在到宿主机上  
方案：将/var/lib/awx/projects 映射到宿主机目录  /data/wwwroot/awx/projects

#### awx_redis 容器无法启动？

原因：redis.sock 权限不足导致  
方案：给 /data/.awx/redis_socket 文件夹授权

1. 编辑 */data/.awx/redis.conf* 文件中增加一行权限配置 `unixsocketperm 750`
   ```
   unixsocket /var/run/redis/redis.sock
   unixsocketperm 660
   port 0
   bind 127.0.0.1
   unixsocketperm 750
   ```
2. Redis 通信目录授权 `chmod -R 777 /data/.awx/redis_socket`
3. 进入到 AWX 目录后，重新运行容器即可
   ```
   cd /data/.awx
   docker-compose down -v
   docker-compose up -d
   ```

#### 能够正常进入 AWX 控制台，但无法运行 Job？

很有可能是 awx_redis 容器没有正常运行导致，通过命令 `docker ps` 查看 awx_redis 运行状态
