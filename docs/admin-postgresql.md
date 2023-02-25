# PostgreSQL 

AWX deployment package includes PostgreSQL, refer to these steps to use it:

1. Use **SSH** to connect Server, run the command `docker ps` to list all containers
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-getcontainerid-websoft9.png)

2. Get the ID number of **awx-postresql** and run `exec` command to connect it

   ```
   docker exec -it true 2ca9ad211678 /bin/bash
   ```
3. Now, you can use any PostgreSQL commands for management

> Websoft9 provide *[PostgreSQL guide](https://support.websoft9.com/docs/postgresql/admin-phppgadmin.html)* for more useful skills of PostgreSQL, includes: modify password, create user, import/export data, enable or disable remote visit, log configuration and so on.