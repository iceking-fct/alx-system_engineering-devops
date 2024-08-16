#!/urs/bin/env bash
# Making changes to our configuration file using Puppet.

file {'/etc/ssh/ssh_config':
  ensure  => 'present',

}

file_line {'Refuse password authentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => 'true',

}

file_line {'Declare  Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',

}
