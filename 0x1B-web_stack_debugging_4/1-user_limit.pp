# THIS CODE Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.


# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard nofile/c\\holberton hard nofile 50000' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/^holberton soft nofile/c\\holberton soft nofile 50000' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

