# FAQ

#### AWX support multi-language?

Yes, it supported [Locales](https://docs.ansible.com/ansible-tower/latest/html/release-notes/supported_locales.html). It automatically sets the locale preference based on the user’s browser settings. For Safari, Internet Explorer, and older versions of Chrome as well as FireFox, this is handled automatically.

#### How is AWX connected to PostgreSQL?

AWX connect PostgreSQL in Docker inner, and you can use external Database

#### AWX support Ansible Galaxy?
Yes, refer to [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)

#### AWX support **var-prompt**?

Yes, refer to [Extra variable](/solution-more.md#extra-variable) charter of this docs

#### What's URL of AWX API?

http://AWX Server Internet IP/api/

#### If there is no domain name, can I deploy AWX?

Yes, visit AWX by *http://Internet IP*

#### What is the password for the database postgres user?

The password is stored in the server related file: `/credentials/password.txt`

#### Is there a web-base GUI database management tools?

No

#### Is it possible to modify the source path of AWX?

No

#### What's the difference between Deployment and Installation?

- Deployment is a process of installing and configuring a sequence of software in sequence in a different order, which is a complex system engineering.  
- Installation is the process of starting the initial wizard after the application is prepared.  
- Installation is simpler than deployment. 

#### What's Cloud Platform?

Cloud platform refers to platform manufacturers that provide cloud computing services, such as: **Azure, AWS, Alibaba Cloud, HUAWEI CLOUD, Tencent Cloud**, etc.

#### What is the difference between Instance, Cloud Server, Virtual Machine, ECS, EC2, CVM, and VM?

No difference, just the terminology used by different manufacturers, actually cloud servers