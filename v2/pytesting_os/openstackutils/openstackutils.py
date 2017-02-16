#!/usr/bin/env python
#-*- coding: utf-8 -*-
from openstackutils import OpenStackUtils
import time, re, paramiko, os
from os import environ as env


def get_cloud():
    return OpenStackUtils()


def boot_vm_with_userdata_and_port(keypair,userdata_path):
    nics = [{'port-id': env['NOSE_PORT_ID']}]
    server = get_cloud().nova_client.servers.create(name="test-server-" + current_time_ms(), image=env['NOSE_IMAGE_ID'],security_groups=[env['NOSE_SG_ID']],
                                                    flavor=env['NOSE_FLAVOR'], key_name=keypair.id, userdata=file(userdata_path), nics=nics)

    time.sleep(80)

    return server


def boot_vm(keypair,image_id=env['NOSE_IMAGE_ID'],flavor=env['NOSE_FLAVOR']):
    nics = [{'net-id': env['NOSE_NET_ID']}]
    server = get_cloud().nova_client.servers.create(name="test-server-" + current_time_ms(), image=image_id,security_groups=[env['NOSE_SG_ID']],
                                                    flavor=flavor, key_name=keypair.id, nics=nics)

    time.sleep(80)

    return server


def get_server(server_id):
    return get_cloud().nova_client.servers.get(server_id)


def destroy_server(server):
    get_cloud().nova_client.servers.delete(server)


def current_time_ms():
    return str(int(round(time.time() * 1000)))


def get_console_log(server):
    return get_cloud().nova_client.servers.get(server.id).get_console_output(length=200)


def get_spice_console(server):
    return get_cloud().nova_client.servers.get(server.id).get_spice_console('spice-html5')


def create_server_snapshot(server):
     k=get_cloud().nova_client.servers.create_image(server,server.name+current_time_ms())
     print k
     return k

def get_image(image_id):
    return get_cloud().glance_client.images.get(image_id)


def destroy_image(image_id):
    get_cloud().glance_client.images.delete(image_id)


def initiate_ssh(floating_ip,keypair):
    counter = 0
    while counter < 30:
        counter += 1
        try:
            ssh_connection = paramiko.SSHClient()
            ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print floating_ip.ip
            tmp=current_time_ms()
            print keypair.private_key
            fp = os.open(env['HOME']+'/private_key-'+tmp+'.pem', os.O_WRONLY | os.O_CREAT, 0o600)
            with os.fdopen(fp, 'w') as f:
                f.write(keypair.private_key)
            ssh_connection.connect(
                floating_ip.ip,
                username='cloud',
                key_filename=env['HOME']+'/private_key-'+tmp+'.pem',
                timeout=180
            )

            chan_in, chan_out, chan_err = ssh_connection.exec_command("cat /etc/passwd")
            data = chan_out.read()
            print data
            return ssh_connection
        except paramiko.ssh_exception.NoValidConnectionsError:
            time.sleep(6)
            pass

    return None


def create_floating_ip():
    floating_ip = get_cloud().nova_client.floating_ips.create('public')
    return floating_ip


def associate_floating_ip_to_port(floating_ip):
    get_cloud().neutron_client.update_floatingip(floating_ip.id,{'floatingip': {'port_id': env['NOSE_PORT_ID'] }})


def associate_floating_ip_to_server(floating_ip, server):
    get_cloud().nova_client.servers.get(server.id).add_floating_ip(floating_ip.ip)


def delete_floating_ip(floating_ip):
    get_cloud().nova_client.floating_ips.delete(floating_ip.id)


def rescue(server):
    get_cloud().nova_client.servers.get(server.id).rescue()


def attach_volume_to_server(server):
    get_cloud().nova_client.volumes.create_server_volume(server.id, env['NOSE_VOLUME_ID'])


def detach_volume_from_server(server):
    get_cloud().nova_client.volumes.delete_server_volume(server.id,env['NOSE_VOLUME_ID'])


def get_flavor_disk_size(flavor_id):
    return get_cloud().nova_client.flavors.get(flavor_id).disk


def hard_reboot(server):
    get_cloud().nova_client.servers.get(server.id).reboot(reboot_type='HARD')
    time.sleep(60)


def soft_reboot(server):
    get_cloud().nova_client.servers.get(server.id).reboot(reboot_type='SOFT')
    time.sleep(60)


def create_keypair():
    keypair= get_cloud().nova_client.keypairs.create("testkeypair-"+current_time_ms())
    print keypair.private_key
    return keypair


def delete_keypair(keypair):
    get_cloud().nova_client.keypairs.delete(keypair.id)

