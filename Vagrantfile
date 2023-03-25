# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.define 'ubuntu20' do |builder|
    builder.vm.box = 'ubuntu/focal64'
    builder.ssh.insert_key = false
    builder.vm.disk :disk, size: '50GB', primary: true
    builder.vm.box_version = '20221107.0.0'
    builder.vm.provider 'virtualbox' do |vb|
      vb.memory = 2048
      vb.cpus = 4
    end
    builder.vm.provision 'shell', inline: <<-SHELL
      set -x
      set -e
      # alter authentication options and change password
      sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      sed -i 's/ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/g' /etc/ssh/sshd_config
      sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
      systemctl restart sshd.service
      echo root:root | chpasswd
    SHELL
  end
end
