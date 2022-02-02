# Simple Kubernetes cluster ansible install

Prerequisites:
- installed physical or virtual hosts with Debian-like (preferably Debian 11) systems
- existsing user "ansible" with "no password" sudo on all host
- public key of installer user is in the ansible user's .ssh/authorized_keys file
- authentication by public key is allowed in the sshd configuration
- ansible (and ansible-playbook) is installed on the install/bastion/ansible/etc host


Prepare before install:
- fill out the inventory.yaml file with relevant information for your environment

Install:
- execute the following command in the root directory:
ansible-playbook -i inventory.yaml install_k8s.yaml
