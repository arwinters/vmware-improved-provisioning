#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Anthony Winters <info@nforce-it.nl>


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: nforce_vm

short_description: This simple module converts metadata and userdata into gzip+base64 for cloud-init VM customization.

version_added: "2.9"

description:
    - "This simple module can converts metadata and userdata into gzip+base64"

options:
    metadata:
        description:
            - The metadata in YAML or JSON in string format
        required: true
    userdata:
        description:
            - The userdata in YAML or JSON in string format
        required: true        

extends_documentation_fragment:
    - nforce_vm

author:
    - A.R. Winters <info@nforce-it.nl>
'''

EXAMPLE = '''
- nforce_vm:
    metadata: "{{ lookup('template', 'test/metadata.yaml') }}"
    userdata: "{{ lookup('file', 'test/userdata.yaml') }}"
  register: vm_cloud_init
'''

RETURN = '''
{
  "metadata":
  "userdata":
  "changed":
}
'''

from ansible.module_utils.basic import AnsibleModule
import gzip
import base64


def _convert(module):

    metadata_yaml = module.params['metadata']
    userdata_yaml = module.params['userdata']

    try:
        metadata_base64 = base64.b64encode(gzip.compress(metadata_yaml.encode('utf-8'), 9)).decode('utf-8')
        userdata_base64 = base64.b64encode(gzip.compress(userdata_yaml.encode('utf-8'), 9)).decode('utf-8')

    except Exception as e:
        module.fail_json(changed=False, exception=e, msg="Converting metadata and userdata failed.")

    results = {
        "changed": "true",
        "metadata": metadata_base64,
        "userdata": userdata_base64,
    }
    module.exit_json(**results)


def main():
    module_args = dict(
        metadata=dict(type="str", required=True),
        userdata=dict(type="str", required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
    )

    _convert(module)


if __name__ == '__main__':
    main()
