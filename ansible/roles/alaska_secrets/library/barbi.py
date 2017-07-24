#!/usr/bin/env python

# import some python modules that we'll use.  These are all
# available in Python's core

ANSIBLE_METADATA = {'metadata_version': '1.0'}

import sys
import json
import os

from barbicanclient import client
from keystoneauth1 import identity
from keystoneauth1 import session


def main():
    module = AnsibleModule(
        argument_spec = dict(
            key=dict(required=True, type='str'),
        ),
        supports_check_mode=False
    )

    # Keystone V3 password authentication
    auth = identity.V3Password(auth_url=os.getenv('OS_AUTH_URL'),
			       username=os.getenv('OS_USERNAME'),
			       user_domain_name=os.getenv('OS_USER_DOMAIN_NAME', 'Default'),
			       password=os.getenv('OS_PASSWORD'),
			       project_name=os.getenv('OS_PROJECT_NAME'),
			       project_domain_name=os.getenv('OS_PROJECT_DOMAIN_NAME','Default'))
    sess = session.Session(auth=auth)
    barbican = client.Client(session=sess)
    if not barbican:
        module.fail_json(msg="Unable to initialise Barbican client")

    secret_key = module.params['key']
    secret_list = barbican.secrets.list(name=secret_key)
    if secret_list:
	retrieved_secret = secret_list[0].payload
        module.exit_json(changed=True, secret=retrieved_secret)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
