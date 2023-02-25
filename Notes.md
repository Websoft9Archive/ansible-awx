
## AWX-CLI



实际安装命令解决问题。

` pip install ansible-tower-cli`



```shell
tower-cli config host http://127.0.0.1

tower-cli config username  admin	# 设置登录名

tower-cli config password VZ6gWlscqnFoxvm # 设置登录密码

tower-cli config verify_ssl False #设置是否使用ssl登录，False使用http登录，True使用Https登录

tower-cli user list ## 测试是否成功，成功的话显示用户
```



***遇到错误***

1. Error: Can not verify ssl with non-https protocol. Change the verify_ssl configuration setting to continue.

解决方法：配置`root/.tower_cli.cfg`文件，将verify_ssl配置项目设置为false

```cfg
[general]
host = http://127.0.0.1
username = admin
password = VZ6gWlscqnFoxvm
verify_ssl: False
```
