##Role Name
  =========

Tomcat Role :- it installed tomcat versions 7, 8, 8.5 and 9.

##Requirements
  ------------

Java must be pre installed and java version must be compatible for installing tomcat version.

##Role Variables
  --------------

Variable are defined in defaults/main.yml and must be verfied before executing the role.

Ansible vault is configured for this role.

##Example Playbook
  ----------------
```
- hosts: local
  vars:
    tomcat_version: 8.5.23
    ansible_become: yes
    ansible_become_pass: "{{ my_sudo_pass }}"
    
    
    tomcat_users:
      - username: "tomcat"
        password: "t3mpp@ssw0rd"
        roles: "tomcat,admin,manager,manager-gui"
      - username: "exampleuser"
        password: "us3rp@ssw0rd"
        roles: "tomcat"        
  roles:
    - role: tomcat

ansible-playbook tomcat.yml --ask-vault-pass --extra-vars '@passwd.yml'
```

##License
  -------

Apache

##Author Information
  ------------------

Name :- Rohit Bansal
Email :- rohit.bansal@opstree.com