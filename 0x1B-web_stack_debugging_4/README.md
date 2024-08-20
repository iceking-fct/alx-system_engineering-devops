##THIS README FILE CONTAIN THE DESCRIPTION FOR THE 0x1B. Web stack debugging #4 TASK GIVEN BY ALX##


- AUTHUR: MIRACLE AMAJAMA (https://github.com/iceking-fct)


- Project started August 19, 2024 6:00 AM, must end by Aug 23, 2024 6:00 AM
Checker will be released at Aug 22, 2024 6:00 AM
An auto review will be launched at the deadline

 


-Requirements
General

    All your files will be interpreted on Ubuntu 14.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp
    Files will be checked with Puppet v3.4

- Install puppet-lint

$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1



Tasks
0. Sky is the limit, let's bring that limit higher
mandatory

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends! 




Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x1B-web_stack_debugging_4
    File: 0-the_sky_is_the_limit_not.pp





- 
1. User limit
#advanced

Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.




Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x1B-web_stack_debugging_4
    File: 1-user_limit.pp


