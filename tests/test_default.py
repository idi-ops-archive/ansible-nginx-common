import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')

def test_nginx_config_file(File):
    f = File('/etc/nginx/nginx.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644

def test_nginx_service(Service):
    s = Service('nginx')

    assert s.is_enabled
    assert s.is_running

def test_sshd_process(Process):
    p = Process.filter(user='root', comm='nginx')

    assert len(p) >= 1

# FIX: Port to be tested should be retrieved from Ansible variables
def test_sshd_socket(Socket):
    s = Socket("tcp://0.0.0.0:80")

    assert s.is_listening
