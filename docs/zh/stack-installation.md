# 初始化安装

在云服务器上部署 AWX 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 AWX，请先到 **域名控制台** 完成一个域名解析

## AWX 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://公网IP*, 进入 AWX 登录页面
   ![AWX登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-login-websoft9.png)

3. 输入用户名和密码[（不知道密码？）](/zh/stack-accounts.md)，登录到 AWX 后台管理界面
   ![AWX后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-gui-websoft9.png)

4. 此时，AWX 安装部署已经验证通过

> 需要了解更多AWX的使用，请参考：[Ansible Tower Documentation](https://docs.ansible.com/ansible-tower/).

## AWX 入门向导

现在开始针对于**如何使用 AWX 可视化运行 Ansible 项目**进行完整的实战操作说明：

### 概念

在实战之前，必须先了解几个概念：

![AWX后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-consoleui-websoft9.png)

* **清单（Inventories）**：对应 Ansible 的 Inventory，即主机组和主机IP清单列表。

* **凭证（Credentials）**：受控主机的用户名、密码（秘钥）以及提权控制

* **项目（Projects）**：一个完整可运行的 Ansible 项目

* **模板（Templates）**：将清单、项目和凭证关联起来的任务模板，一次创建，多次使用，可修改

* **作业（Jobs）**：模板每一次运行视为一次作业

### 准备

在使用 AWX 运行一个 Ansible 项目之前，请确保符合如下条件：

* 准备一个可用的 Ansible 项目，例如：[Grafana](https://github.com/Websoft9/ansible-grafana)
* 准备一台新创建的云服务器，此服务器被 AWX 安装 Ansible 项目。建议先运行下面的脚本，在服务中安装主流的仓库，以及 Git,pip 等工具
  ```
  wget -N https://cdn.statically.io/gh/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh
  ```

### 步骤

下面我们开始列出具体的步骤：

1. 登录 AWX，创建【清单】，然后在清单中增加【主机】

   ![创建清单](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-inventories001-websoft9.png)

   ![创建主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-inventories002-websoft9.png)

   ![创建主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-inventories003-websoft9.png)

2. 创建【凭证】，下面是创建一个 root 账号以及管理密码所对应的范例（凭证类型选择【机器】）
   ![创建凭证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-credentials-websoft9.png)

3. 创建【项目】，下面以我们提供的开源项目 [HelloWorld](https://github.com/ansible/tower-example) 作为范例

   ![创建项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-project-websoft9.png)

4. 创建【模板】，分别将前面创建的【凭证】、【清单】、【项目】关联起来，便完成了模板的配置
   ![创建模板](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-templates-websoft9.png)

   > 也可以直接设置**额外变量**覆盖交互式

6. 启动Template，进入 Job 页面，开始安装所需的应用程序
   ![成功运行项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-templaterunning-websoft9.png)

## 常见问题

#### 浏览器打开IP地址，无法访问 AWX（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 AWX 数据？

PostgreSQL Docker

#### AWX 是否支持 Ansible Galaxy？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-setgalax-websoft9.png)

支持，参考官方文档 [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)