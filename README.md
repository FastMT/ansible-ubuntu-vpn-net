# ubuntu-vpn-net
Ansible role to create VPN network betweeen linux (Ubuntu) servers

## Installation

Create requirements.yml file

```
# Include ubuntu-common role
- src: https://github.com/FastMT/ansible-ubuntu-vpn-net.git
  name: ubuntu-vpn-net
  version: "v1.0.0"
```

Install external module into ~/.ansible/roles folder

```
ansible-galaxy install -r requirements.yml
```

## Usage

playbook.yml:

```
# Create VPN network betweeen servers
- role: "ubuntu-vpn-net"
    vars:
      # Optional parameter - not ask password on sudo (default: yes)
      sudo_nopasswd: yes

      # Optional parameter - sysctl config
      linux_sysctl:
        - { name: "systctl.config.parameter",     value: 1 }      
```   
