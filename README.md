# osm_tomcat
  

`This role installed tomcat versions 7, 8 and 8.5. it checks for java version dependency`
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

`Java must be pre installed and java version must be compatible for installing tomcat version.`


# Role Variables
 --------------

`variables defined in vars/main.yml`
```
* tomcat_version: Tomcat version which needs to install eg: 8.5.23
* tomcat_user: User name by which tomcat will run
* tomcat_group: Group name by which tomcat will be accessible
* tomcat_service_name: Service name of tomcat
* tomcat_port_connector: Port no. on which tomcat will be accessible
* tomcat_jvm_memory_percentage_xms: Min memory to tomcat process
* tomcat_jvm_memory_percentage_xmx: Max memory to tomcat process
```

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