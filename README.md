# osm_tomcat
  

 This role installed tomcat versions 7, 8 and 8.5. it checks for java version dependency
```
 Tomcat Version | Java Version
 ------------------------------
     7.0        | 6 or later
     8.0        | 7 or later
     8.5        | 7 or later
```

# Supported OS  

```
Redhat 6/7
Centos 6/7
Ubuntu 14/16
Amazon Linux
```
 
# Requirements

Java must be pre installed and java version must be compatible for installing tomcat version.


# Role Variables
 --------------

Available variables can be explored in [vars](https://gitlab.com/oosm/osm_tomcat/blob/master/vars/main.yml)


# Example Playbook
  
```
- hosts: local

  roles:
    - role: osm_tomcat

ansible-playbook tomcat.yml
```

# License
```
Apache
```

# Author Information
  
```
Name :- Rohit Bansal
Email :- rohit.bansal@opstree.com
```