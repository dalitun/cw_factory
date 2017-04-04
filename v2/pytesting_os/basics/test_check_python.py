from basics import test_resources

def test_python():
    global test_resources

    ssh_stdin, ssh_stdout, ssh_stderr = test_resources['ssh_connection'].exec_command('python --version')
    ssh_python = ssh_stdout.read()
    check_python = (ssh_python.find('Python 2') != -1)
    assert check_python