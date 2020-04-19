from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_config

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

def deploy_vlan(task):
    task.run(task=netmiko_send_config, config_commands= ["vlan 43", "name Management", "vlan 55", "name Guest", "vlan 99", "name Office"])

results = nr.run(task = deploy_vlan)

print_title("VLANS DEPLOYED")
print_result(results)
