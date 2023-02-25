# PostgreSQL

AWX 预装包中内置 PostgreSQL 容器，需要登录容器后使用命令对 PostgreSQL 进行操作。

1. 使用 SSH 登录服务器后，运行`docker ps`命令获取 awx-postresql 容器ID
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-getcontainerid-websoft9.png)

2. 进入 awx-postgresql 容器

   ```
   docker exec -it 2ca9ad211678 /bin/bash
   ```
4. 运行上面的命令后，就进入了容器命令操作界面

5. 接下来可以使用命令操作 PostgreSQL 

> 阅读Websoft9提供的 [《PostgreSQL教程》](https://support.websoft9.com/docs/postgresql/zh/) ，掌握更多的PostgreSQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等
