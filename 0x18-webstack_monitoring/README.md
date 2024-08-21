verview #
*“You cannot fix or improve what you cannot measure”* is a famous saying in the Tech industry. In the age of the *data-ism*, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

1. **Application monitoring:** getting data about your running software and making sure it is behaving as expected
2. **Server monitoring:** getting data about your virtual or physical server and making sure they are not overloaded; (could be CPU, memory, disk or network overload).

Most of the work on this project was done on our Monitoring agent [Datadog](https://www.datadoghq.com/) and cannot be included here. However, the work involved:
    1. Creating a free account on [Datadog](https://www.datadoghq.com/).
    2. Creating application and api keys
    3. Installing the datadog agent on our remote server
    4. Setting up Monitors and alerts for various information, including *IO:writes/sec* and *IO:reads/sec*.
    5. Creating a dashboard on our Account
    6. Accessing our account information/data via the [API](api.datadog.hq).<br/>

## Objectives ##
- Why is monitoring needed
- What are the 2 main area of monitoring
- What are access logs for a web server (such as Nginx)
- What are error logs for a web server (such as Nginx)<br/>


## General Project Requirements ##
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension<br/>


## Folder Details ###
- **Date Created:**Wednesday, August 21  2024.
- **Author:** [MIRACLE AMAJAMA](https.//github.com/iceking-fct).
- **Project Timeline:**
  - **Released:** Wed Aug 14 2024 - 6am.
  - **1st Deadline:** Thur Aug 15 2024 - 6am.
  - **Duration:** 24 hrs.<br/>


## Reference Resources ##
- [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
- [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
- [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)<br/>

## File Tree ##
.<br/>
├── 2-setup_datadog<br>
└── README.md<br>
<br/>
1 directories, 2 files<br/>


## Files ###
- *Below is the  list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [2-setup_datadog](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x18-webstack_monitoring/2-setup_datadog) | A file containing the id of our [Datadog](https://www.datadoghq.com/) dashboard for our server `179755-web-01`.|

