# Ansible Collection - my_own_namespace.yandex_cloud_elk

## Overview
This collection provides a custom module and role that create a text file on a target host with the specified content.

## Requirements
- Ansible Core

## Included content

### Module: `my_own_module`
Creates a text file at a given path with the provided content.

**Parameters**
- `path` (str, required): Destination path for the file.
- `content` (str, required): Text to write into the file.

**Example**
```yaml
- name: Create file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_own_module.txt
    content: hello world
```

### Role: `my_own_role`
Wraps the module into a role with defaults.

**Defaults**
- `my_own_module_path`: `/tmp/my_own_module.txt`
- `my_own_module_content`: `hello world`

**Example**
```yaml
- name: Test my_own_role
  hosts: localhost
  gather_facts: false
  roles:
    - role: my_own_role
```

## Local testing
Use `inventory.ini`, `playbook.yml` (single task), or `playbook_role.yml` (role).
