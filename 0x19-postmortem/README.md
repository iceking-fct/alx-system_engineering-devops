### Postmortem: Nginx Service Outage on Ubuntu Container

#### Issue Summary:
- **Duration:** The outage lasted for approximately 45 minutes, from 10:00 AM to 10:45 AM UTC.
- **Impact:** The Nginx service on an Ubuntu container was not responding on port 80, affecting 100% of the users trying to access the web server hosted on this container. Users experienced an inability to load the web pages served by Nginx, resulting in downtime for all services dependent on this server.
- **Root Cause:** The root cause was a misconfiguration in the Nginx configuration files, where the default server block was not properly enabled, preventing Nginx from listening on port 80.

#### Timeline:
- **10:00 AM UTC:** Issue detected via a monitoring alert indicating that the web server was down.
- **10:05 AM UTC:** Initial investigation began by checking the status of the Nginx service and confirming that it was not responding on port 80.
- **10:10 AM UTC:** Checked Nginx logs for any obvious errors; however, no critical errors related to port binding were found.
- **10:15 AM UTC:** Assumed the issue might be related to a recent update or firewall configuration, but these paths did not reveal any problems.
- **10:25 AM UTC:** The issue was escalated to the DevOps team for further investigation.
- **10:30 AM UTC:** DevOps team identified the problem as a misconfigured default server block in the Nginx configuration.
- **10:35 AM UTC:** A fix was applied by enabling the correct configuration and restarting the Nginx service.
- **10:45 AM UTC:** Nginx was confirmed to be listening on port 80, and the service was fully restored.

#### Root Cause and Resolution:
The root cause of the outage was traced back to an incorrect configuration in the Nginx server block. The default server block configuration in `/etc/nginx/sites-available/default` was not properly linked to `/etc/nginx/sites-enabled/`, resulting in Nginx not binding to port 80. This misconfiguration caused Nginx to fail in serving web requests on the standard HTTP port.

The issue was resolved by copying the correct configuration file from `/etc/nginx/sites-available/` to `/etc/nginx/sites-enabled/`, ensuring that the server was configured to listen on port 80. The Nginx service was then restarted using the command `sudo service nginx restart`, which reloaded the configuration and restored the service.

#### Corrective and Preventative Measures:
To prevent similar issues in the future, the following actions will be taken:

1. **Configuration Management:** Implement automated checks to ensure that the necessary server blocks are correctly configured and enabled in Nginx.
2. **Monitoring and Alerts:** Enhance monitoring to detect misconfigurations in Nginx earlier and provide more detailed alerts regarding service disruptions.
3. **Documentation:** Update internal documentation to include a checklist for validating Nginx configurations during deployments or updates.
4. **Automation Script:** Develop a Bash script to automate the process of checking and correcting Nginx configuration issues before restarting the service.

**Specific Tasks:**
- [ ] Create a configuration validation script for Nginx.
- [ ] Implement automated deployment scripts that include Nginx configuration checks.
- [ ] Set up enhanced monitoring to detect when Nginx is not listening on its expected ports.
- [ ] Review and update all server configurations to ensure consistency across environments.

This postmortem aims to improve the resilience of our web stack and prevent future outages by addressing the root cause and implementing preventative measures.
