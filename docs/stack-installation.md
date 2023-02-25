# Initial Installation

If you have completed the AWX deployment on Cloud Platform, the following steps is for you to start use it quikly

## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check you **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the TCP:80 is allowed
3. Make a domain resolution on your DNS Console if you want to use domain for AWX

## AWX Installation Wizard

1. Using local browser visit the URL *http://DNS* or *http://Server's Internet IP*, enter to login interface
   ![AWX login page](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-login-websoft9.png)

2. Login it to AWX console [(Don't know password?)](/stack-accounts.md#awx)
   ![AWX console](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awxui-websoft9.png)

> More useful AWX guide, please refer to [Ansible Tower Documentation](https://docs.ansible.com/ansible-tower/)

## AWX Setup wizard

Now, we will give use sample **How to run Ansible repository by AWX** for your practice

### Concept

You must understand some import concept before your practice:

![AWX console](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awxui-websoft9.png)

* **Inventories**: A list of managed nodes

* **Credentials**: Username and password or key of nodes

* **Projects**: Ansible project, most of time it is a Github repository

* **Templates**: It is a definition and set of parameters for running an Ansible job

* **Jobs**: It is an instance of Tower launching an Ansible playbook against an inventory of hosts.

### Prepare

Before using AWX to run an Ansible project, please ensure that the following conditions are met:

* Prepare your Ansible project, e.g. [Grafana](https://github.com/Websoft9/ansible-grafana)
* Prepare your one node and run the following command for runtime preparation
  ```
  wget -N https://cdn.statically.io/gh/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh
  ```

### Steps

Below we begin to list the specific steps:

1. Login AWX and create 【Inventories】, then add 【Host】 in it.

   ![create Inventories](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-inventories001-websoft9.png)

   ![create host](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-inventories002-websoft9.png)

   ![create host](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-inventories003-websoft9.png)

2. Create 【Credentials】, the following example
   ![Create Credentials](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-credentials-websoft9.png)

3. Create 【Project】, the following example is use [Grafana](https://github.com/Websoft9/ansible-grafana) powered by Websoft9

   ![create Project](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-project-websoft9.png)

4. Create 【Templates】, associate 【Credentials】,【Inventories】,【Project】 in one interface
   ![Create template](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-templates-websoft9.png)

   > You can set it by add **extra variable** directly

5. Go to Template and start a 【Job】
   ![Job running](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-templaterunning-websoft9.png)

## Q&A 

#### I can't visit the start page of AWX?

Your TCP:80 of Security Group Rules is not allowed so there no response from Chrome or Firefox

#### Which database does this AWX use?

PostgreSQL on Docker

#### Is AWX support Ansible Galaxy?

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-setgalax-websoft9.png)
Yes, refer to official docs [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)