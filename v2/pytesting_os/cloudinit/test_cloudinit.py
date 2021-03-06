from cloudinit import test_resources


global test_resources

def test_cloudinit_package():
    ssh_stdin, ssh_stdout, ssh_stderr = test_resources['ssh_connection'].exec_command('vi --version')
    cmd_stdout = ssh_stdout.read()
    package_installed_by_userdata_is_present = (cmd_stdout.find('vi') != -1)
    print "Vi IMproved" + cmd_stdout

    assert package_installed_by_userdata_is_present


def test_cloudinit_runcmd():
    ssh_stdin, ssh_stdout, ssh_stderr = test_resources['ssh_connection'].exec_command('sudo ls /etc')
    cmd_stdout= ssh_stdout.read()
    file_created_by_userdata_is_present = (cmd_stdout.find('hosts') !=-1)
    assert file_created_by_userdata_is_present

