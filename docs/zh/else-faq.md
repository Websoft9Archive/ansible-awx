# FAQ

#### AWX支持多语言吗？

支持[多种语言](https://docs.ansible.com/ansible-tower/latest/html/release-notes/supported_locales.html)，包括中文。它不提供语言切换菜单，而是自动适用浏览器首选语言。

#### AWX是如何与PostgreSQL连接的？

容器内部连接，即容器编排

#### AWX 是否支持 Ansible Galaxy？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-setgalax-websoft9.png)

支持，参考官方文档 [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)

#### AWX 是否支持交互式变量？

支持，参考[额外变量](/zh/solution-more.md#额外变量)章节

#### AWX API 地址是多少？

http://AWX Server Internet IP/api/

#### 如果没有域名是否可以部署 AWX？

可以，访问`http://服务器公网IP` 即可

#### 数据库 Postgres 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

为了安全考虑，没有提供可视化的数据库管理工具

#### 是否可以修改AWX的源码路径？

采用 Docker 安装，不可以修改

#### 部署和安装有什么区别？

部署是将一序列软件按照不同顺序，先后安装并配置到服务器的过程，是一个复杂的系统工程。  
安装是将单一的软件拷贝到服务器之后，启动安装向导完成初始化配置的过程。  
安装相对于部署来说更简单一些。 

#### 云平台是什么意思？

云平台指提供云计算服务的平台厂家，例如：Azure,AWS,阿里云,华为云,腾讯云等

#### 实例，云服务器，虚拟机，ECS，EC2，CVM，VM有什么区别？

没有区别，只是不同厂家所采用的专业术语，实际上都是云服务器