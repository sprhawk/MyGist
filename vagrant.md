
Create a Base Box
=================

Create a Virtual Machine
-------------------------

RAM 384MB, Storage 10~40GB, disable audio, NAT

install OS (Debian)
-------------------

### before packaging: ###
1. apt-get clean
2. install RubyGems with: --no-rdoc --no-ri or
    rm -r "$(gem env gemdir)"/doc/*
3. 
  * Hostname: vagrant-[os-name], e.g. vagrant-debian-lenny
  * Domain: vagrantup.com
  * Root Password: vagrant
  * Main account login: vagrant
  * Main account password: vagrant
4. main user account should have password-less `sudo` privileges
    %admin ALL=NOPASSWD: ALL
    > Disable `requiretty`
5. set `env_keep` variable to `SSH_AUTH_SOCK`
6. Install VirtualBox Guest Additions
7. install Ruby, RubyGems, Puppet, Chef, SSH






