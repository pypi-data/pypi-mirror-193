#
# Copyright Cloudlab URV 2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

logger = logging.getLogger(__name__)

DEFAULT_REQUIREMENTS = [
    'numpy',
    'requests',
    'redis',
    'pika',
    'cloudpickle',
    'ps-mem',
    'tblib'
]

AVAILABLE_PY_RUNTIMES = {
    '3.6': 'python3.6',
    '3.7': 'python3.7',
    '3.8': 'python3.8',
    '3.9': 'python3.9'
}

USER_RUNTIME_PREFIX = 'lithops.user_runtimes'

DEFAULT_CONFIG_KEYS = {
    'runtime_timeout': 180,  # Default: 180 seconds => 3 minutes
    'runtime_memory': 256,  # Default memory: 256 MB
    'max_workers': 1000,
    'worker_processes': 1,
    'invoke_pool_threads': 64,
    'architecture': 'x86_64',
    'ephemeral_storage': 512,
    'env_vars': {},
    'vpc': {'subnets': [], 'security_groups': []},
    'efs': []
}

REQ_PARAMS1 = ('access_key_id', 'secret_access_key')
REQ_PARAMS2 = ('execution_role', 'region_name')

RUNTIME_TIMEOUT_MAX = 900  # Max. timeout: 900 s == 15 min
RUNTIME_MEMORY_MIN = 128  # Max. memory: 128 MB
RUNTIME_MEMORY_MAX = 10240  # Max. memory: 10240 MB

RUNTIME_TMP_SZ_MIN = 512
RUNTIME_TMP_SZ_MAX = 10240


def load_config(config_data):
    if 'aws' not in config_data:
        raise Exception("'aws' section is mandatory in the configuration")

    for param in REQ_PARAMS1:
        if param not in config_data['aws']:
            msg = f'"{param}" is mandatory in the "aws" section of the configuration'
            raise Exception(msg)

    if not config_data['aws_lambda']:
        raise Exception("'aws_lambda' section is mandatory in the configuration")

    for param in REQ_PARAMS2:
        if param not in config_data['aws_lambda']:
            msg = f'"{param}" is mandatory in the "aws_lambda" section of the configuration'
            raise Exception(msg)

    for key in DEFAULT_CONFIG_KEYS:
        if key not in config_data['aws_lambda']:
            config_data['aws_lambda'][key] = DEFAULT_CONFIG_KEYS[key]

    if config_data['aws_lambda']['runtime_memory'] > RUNTIME_MEMORY_MAX:
        logger.warning("Memory set to {} - {} exceeds "
                       "the maximum amount".format(RUNTIME_MEMORY_MAX, config_data['aws_lambda']['runtime_memory']))
        config_data['aws_lambda']['runtime_memory'] = RUNTIME_MEMORY_MAX

    if config_data['aws_lambda']['runtime_memory'] < RUNTIME_MEMORY_MIN:
        logger.warning("Memory set to {} - {} is lower than "
                       "the minimum amount".format(RUNTIME_MEMORY_MIN, config_data['aws_lambda']['runtime_memory']))
        config_data['aws_lambda']['runtime_memory'] = RUNTIME_MEMORY_MIN

    if config_data['aws_lambda']['runtime_timeout'] > RUNTIME_TIMEOUT_MAX:
        logger.warning("Timeout set to {} - {} exceeds the "
                       "maximum amount".format(RUNTIME_TIMEOUT_MAX, config_data['aws_lambda']['runtime_timeout']))
        config_data['aws_lambda']['runtime_timeout'] = RUNTIME_TIMEOUT_MAX

    if not {'subnets', 'security_groups'}.issubset(set(config_data['aws_lambda']['vpc'])):
        raise Exception("'subnets' and 'security_groups' are mandatory sections under 'aws_lambda/vpc'")

    if not isinstance(config_data['aws_lambda']['vpc']['subnets'], list):
        raise Exception("Unknown type {} for 'aws_lambda/"
                        "vpc/subnet' section".format(type(config_data['aws_lambda']['vpc']['subnets'])))

    if not isinstance(config_data['aws_lambda']['vpc']['security_groups'], list):
        raise Exception("Unknown type {} for 'aws_lambda/"
                        "vpc/security_groups' section".format(type(config_data['aws_lambda']['vpc']['security_groups'])))

    if not isinstance(config_data['aws_lambda']['efs'], list):
        raise Exception("Unknown type {} for "
                        "'aws_lambda/efs' section".format(type(config_data['aws_lambda']['vpc']['security_groups'])))

    if not all(
            ['access_point' in efs_conf and 'mount_path' in efs_conf for efs_conf in config_data['aws_lambda']['efs']]):
        raise Exception("List of 'access_point' and 'mount_path' mandatory in 'aws_lambda/efs section'")

    if not all([efs_conf['mount_path'].startswith('/mnt') for efs_conf in config_data['aws_lambda']['efs']]):
        raise Exception("All mount paths must start with '/mnt' on 'aws_lambda/efs/*/mount_path' section")

    # Lambda runtime config
    if config_data['aws_lambda']['ephemeral_storage'] < RUNTIME_TMP_SZ_MIN \
            or config_data['aws_lambda']['ephemeral_storage'] > RUNTIME_TMP_SZ_MAX:
        raise Exception(f'Ephemeral storage value must be between {RUNTIME_TMP_SZ_MIN} and {RUNTIME_TMP_SZ_MAX}')

    # Put credential keys to 'aws_lambda' dict entry
    config_data['aws_lambda'].update(config_data['aws'])
