# 更新升级

网站技术日新月异，**更新升级**是维护工作之一，长时间不升级的程序，就如长时间不维护的建筑物一样，会加速老化、功能逐渐缺失直至无法使用。  

这里注意更新与升级这两词的差异（[延伸阅读](https://support.websoft9.com/docs/faq/zh/tech-upgrade.html#更新-vs-升级)），例如：
- 操作系统打个补丁常称之为**更新**，Ubuntu16.04 变更为 Ubuntu18.04，称之为**升级**
- MySQL5.6.25-->MySQL5.6.30 常称之为**更新**，MySQL5.6->MySQL5.7 称之为**升级**

AWX 完整的更新升级包括：系统级更新（操作系统和运行环境）和 AWX 程序升级两种类型

## 系统级更新

运行一条更新命令，即可完成系统级更新：

``` shell
#For Ubuntu
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的Cron


## AWX升级

升级AWX通过重新安装来完成。

1. 使用SSH登录服务器
2. 进入到 */data/awx/* 目录，从 Github 更新AWX源码
   ```
   git pull
   ```
3. 进入到 */data/awx/installer* 目录
4. 增加一个 update-vars.yml 文件，其中的内容如下（其中的密码为真实值）：
   ```
   admin_password: 'adminpass'
   pg_password: 'pgpass'
   rabbitmq_password: 'rabbitpass'
   secret_key: 'mysupersecret'
   ```
5. 运行如下命令，开始升级
   ```
   ansible-playbook -i inventory install.yml -e @update-vars.yml
   ```