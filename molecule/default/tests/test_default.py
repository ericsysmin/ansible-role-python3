import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_find_command(host):
    """
    Test to make sure we can find the python3 executable
    """
    exists = host.exists("python3")
    assert exists


def test_run_command(host):
    """
    Test that verify's that python3 works
    """
    cmd = host.run("python3 -V")
    assert cmd.succeeded
