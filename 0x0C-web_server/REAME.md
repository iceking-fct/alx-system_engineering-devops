# Overview #

This project introduces the concepts of **servers**, and how to configure them with **Nginx**.

I love this with my whole heart.

<hr/>

### Learning Objectives ###
It is expected that at the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General ####
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

#### DNS ###
- What DNS stands for
- What is DNS main role

#### DNS Record Types ####
- A
- CNAME
- TXT
- MX

### Requirements and Constraints ###
- Allowed editors: `vi`, `vim`, and `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing
- Can’t use `systemctl` for restarting a process


## Folder Details ###
- **Date Created:** Monday 16Th September, 2024.
- **Author:** [Miracle Amajama](https.//github.com/iceking-fct).
- **Project Timeline:**
  - **Released:** Mon July 1, 2024 - 6am.
  - **1st Deadline:** Wed July 3, 2024 - 6am.
  - **Duration:** 3 days.
  - **Month** 5, **Week** [], **Day** [].


## Reference Resources
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Child process concept page](https://www.notion.so/What-is-a-Child-Process-9716066970b942e1ba72af43b2279c08)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_header_fields.htm)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
- [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

## Useful Commands to `man` or `help`
`scp`, `curl`


## Technologies ##
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- File types can be identified by their extensions
- Code tested on Ubuntu 20.04 LTS.

## File Tree ##
├── 0-transfer_file <br/>
├── 1-install_nginx_web_server <br/>
├── 2-setup_a_domain_name <br/>
├── 3-redirection<br/>
├── 4-not_found_page_404<br/>
├── 7-puppet_install_nginx_web_server.pp<br/>
├── README.md<br/>
├── testtext.sh<br/>
└── text.sh<br/>

*0 directories, 9 files*


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-transfer_file](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/0-transfer_file) | A Bash script that transfers a file from our client to a server: <br /> |
| 2. | [1-install_nginx_web_server](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/1-install_nginx_web_server) | |
| 3. | [2-setup_a_domain_name](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/2-setup_a_domain_name) | |
| 4. | [3-redirection](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/3-redirection) | |
| 5. | [4-not_found_page_404](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/4-not_found_page_404) |  |
| 6. | [7-puppet_install_nginx_web_server.pp](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/7-puppet_install_nginx_web_server.pp)  |  |
| 7. | [README.md](https://github.com/iceking-fct/alx-system_engineering-devops/blob/main/0x0C-web_server/README.md) | |
| 8. | [Others] | Test files - not project dependent. |
