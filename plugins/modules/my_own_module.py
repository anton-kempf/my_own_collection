#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a text file with provided content

version_added: 1.0.0

description:
  - Creates a text file on the target host at the provided path.
  - Writes the provided content into the file.

options:
  path:
    description:
      - Destination path for the file.
    required: true
    type: str
  content:
    description:
      - Text content to write into the file.
    required: true
    type: str

author:
  - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_own_module.txt
    content: hello world
'''

RETURN = r'''
path:
  description: Path of the file written.
  type: str
  returned: always
content:
  description: Content written to the file.
  type: str
  returned: always
changed:
  description: Whether the file was created or updated.
  type: bool
  returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        path='',
        content='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path
    result['content'] = content

    current_content = None
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                current_content = f.read()
        except OSError as exc:
            module.fail_json(msg=f'Failed to read existing file: {exc}', **result)

    would_change = (current_content != content)

    if module.check_mode:
        result['changed'] = would_change
        module.exit_json(**result)

    if would_change:
        parent_dir = os.path.dirname(path)
        if parent_dir:
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except OSError as exc:
                module.fail_json(msg=f'Failed to create parent directory: {exc}', **result)
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        except OSError as exc:
            module.fail_json(msg=f'Failed to write file: {exc}', **result)
        result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
