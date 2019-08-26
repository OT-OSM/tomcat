import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/opt/apache-tomcat-8.5.40/bin')
    assert f.exists
    assert f.user == 'tomcat'
    assert f.group == 'tomcat'

def test_config_file(host):
    f = host.file('/etc/init.d/tomcat')
    ansible_distribution_major_version = host.system_info.distribution
    if  ansible_distribution_major_version == "14":
        assert f.exists
        assert f.is_file
        assert f.user == 'tomcat'
        assert f.group == 'tomcat'
        assert f.mode == '0755'

def test_config_file(host):
    f = host.file('/etc/init.d/tomcat')
    ansible_distribution_major_version = host.system_info.distribution
    if  ansible_distribution_major_version == "6":
        assert f.exists
        assert f.is_file
        assert f.user == 'tomcat'
        assert f.group == 'tomcat'
        assert f.mode == '0755'

def test_service_file(host):
    f = host.file('/etc/systemd/system/tomcat.service')
    ansible_distribution_major_version = host.system_info.distribution
    if  ansible_distribution_major_version == "16":
        assert f.exists
        assert f.user == 'tomcat'
        assert f.group == 'tomcat'
        assert f.mode == '0755'
        assert f.mode == '0755' 

def test_service_file(host):
    f = host.file('/usr/lib/systemd/system/tomcat.service')
    ansible_distribution_major_version = host.system_info.distribution
    if  ansible_distribution_major_version == "7":
         assert f.exists
         assert f.user == 'tomcat'
         assert f.group == 'tomcat'
         assert f.mode == '0755'

def test_svc(host):
    service = host.service("tomcat.service")
    ansible_distribution_major_version = host.system_info.distribution
    if  ansible_distribution_major_version == "16":
        assert service.is_running
        assert service.is_enabled
    ansible_distribution_major_version = host.system_info.distribution
    if  ansible_distribution_major_version == "7":
        assert service.is_running
        assert service.is_enabled

