# AWX CLI

## About

AWX is the official command-line client for AWX and Red Hat Ansible Tower. It:

* Uses naming and structure consistent with the AWX HTTP API
* Provides consistent output formats with optional machine-parsable formats
* To the extent possible, auto-detects API versions, available endpoints, and feature support across multiple versions of AWX and Red Hat Ansible Tower.

Potential uses include:

* Configuring and launching jobs/playbooks
* Checking on the status and output of job runs
* Managing objects like organizations, users, teams, etc…

More detail please refer to the docs：*[**Tower CLI**](https://docs.ansible.com/ansible-tower/latest/html/towercli/index.html)*

##  AWX CLI

#### Install

You should install the AWX CLI like below: 

```
pip install ansible-tower-cli
```

#### Connection
You should completed the AWX CLI connection before use it:

```
tower-cli config host http://<new-awx-host.example.com>
tower-cli config username <user>
tower-cli config password <pass>
tower-cli send assets.json
tower-cli user list # If the test is successful, the user will be displayed
```
> Refer to [Ansible Tower AWX CLI ](https://docs.ansible.com/ansible-tower/latest/html/towercli/usage.html#installation)， [ AWX CLI on AWX Github](https://github.com/ansible/awx/tree/devel/awxkit/awxkit/cli/docs)