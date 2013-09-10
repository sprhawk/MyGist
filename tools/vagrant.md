
Create a Base Box
=================

Create a Virtual Machine
-------------------------

RAM 384MB, Storage 10~40GB, disable audio, NAT

install OS (Debian)
-------------------

### before packaging: ###

    > http://docs-v1.vagrantup.com/v1/docs/base_boxes.html

1. apt-get clean
2. install RubyGems with: --no-rdoc --no-ri or
    rm -r "$(gem env gemdir)"/doc/*
3. 
  * Hostname: vagrant-[os-name], e.g. vagrant-debian-lenny (/etc/hostname, /etc/init.d/hostname start)
  * Domain: vagrantup.com
  * Root Password: vagrant
  * Main account login: vagrant
  * Main account password: vagrant
4. main user account should have password-less `sudo` privileges
    visudo
    %admin ALL=NOPASSWD: ALL
    or %admin ALL=(ALL) NOPASSWD: ALL
    add user vagrant into group admin (create it if needed)
    > Disable `requiretty` if there is Defaults requiretty, then comment it out.
    set `env_keep` variable to `SSH_AUTH_SOCK`
5. Install VirtualBox Guest Additions
6. install Ruby, RubyGems, Puppet, Chef, SSH
7. install emacs, vim, etc
8. SSH:
    * Since Vagrant only supports key-based authentication for SSH, you must setup the SSH user to use key-based authentication. This simply requires copying a public key into ~/.ssh/authorized_keys. (http://github.com/mitchellh/vagrant/tree/master/keys/)
    * In order to keep SSH access speedy even when your host computer can't access the internet, be sure to set UseDNS to no in /etc/ssh/sshd_config. This will disable DNS lookup of clients connecting to the server, which speeds up SSH connection.
9. vagrant package --base virtual_box_name [--vagrantfile vagrantfile]

10. vagrant init boxname

