##README.md##

## Background Context ##
In this project, we set up an application server to serve our **AirBnB_clone** on the web.


## Resources ##
- [Application server vs web server](https://www.f5.com/glossary)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)(don't install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Be careful with the way Flask manages slash in route](https://werkzeug.palletsprojects.com/en/3.0.x/) - *strict_slashes*
- [Upstart documentation](https://doc.ubuntu-fr.org/upstart)<br/>

## Folder Details ###
- **Date Created:** Wed Aug 21 2024.
- **Author:** [Miracle Amajama](https://github.com/iceking-fct).
- **Project Timeline:**
  - **Released:** Mon Aug 19 2024 - 6am.
  - **1st Deadline:** Fri Aug 2024 - 6am.
  - **Duration:** 96hrs(4days).


## Requirements ##
### General ###
- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments
- Bash Scripts
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- All Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts is a comment explaining what is the script doing<br/>



## Reference Resources ##
- WebServer:
  - [Wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server)
  - [Web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)
  - [What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)
- [Troubleshooting a Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)
- [Troubleshooting Apache using strace](https://bobcares.com/blog/troubleshooting-apache-using-strace/)<br/>


## File Tree ##


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-strace_is_r_friend.pp](https://github.com/iceking-fct) | A puppet code that fixes server fail error.|
