from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_send_command

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

def deploy_vlan(task):
    task.run(task=netmiko_send_config, config_file="chris_vlan")

results = nr.run(task = deploy_vlan)

print_title("VLANS DEPLOYED")
print_result(results)
