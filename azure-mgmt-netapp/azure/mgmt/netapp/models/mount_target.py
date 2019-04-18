# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MountTarget(Model):
    """Mount Target.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :param tags: Resource tags
    :type tags: object
    :ivar mount_target_id: mountTargetId. UUID v4 used to identify the
     MountTarget
    :vartype mount_target_id: str
    :param file_system_id: Required. fileSystemId. UUID v4 used to identify
     the MountTarget
    :type file_system_id: str
    :ivar ip_address: ipAddress. The mount target's IPv4 address
    :vartype ip_address: str
    :param subnet: subnet. The subnet
    :type subnet: str
    :param start_ip: startIp. The start of IPv4 address range to use when
     creating a new mount target
    :type start_ip: str
    :param end_ip: endIp. The end of IPv4 address range to use when creating a
     new mount target
    :type end_ip: str
    :param gateway: gateway. The gateway of the IPv4 address range to use when
     creating a new mount target
    :type gateway: str
    :param netmask: netmask. The netmask of the IPv4 address range to use when
     creating a new mount target
    :type netmask: str
    :param smb_server_fqdn: smbServerFQDN. The SMB server's Fully Qualified
     Domain Name, FQDN
    :type smb_server_fqdn: str
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'mount_target_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'file_system_id': {'required': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'ip_address': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'mount_target_id': {'key': 'properties.mountTargetId', 'type': 'str'},
        'file_system_id': {'key': 'properties.fileSystemId', 'type': 'str'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'str'},
        'start_ip': {'key': 'properties.startIp', 'type': 'str'},
        'end_ip': {'key': 'properties.endIp', 'type': 'str'},
        'gateway': {'key': 'properties.gateway', 'type': 'str'},
        'netmask': {'key': 'properties.netmask', 'type': 'str'},
        'smb_server_fqdn': {'key': 'properties.smbServerFqdn', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MountTarget, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.tags = kwargs.get('tags', None)
        self.mount_target_id = None
        self.file_system_id = kwargs.get('file_system_id', None)
        self.ip_address = None
        self.subnet = kwargs.get('subnet', None)
        self.start_ip = kwargs.get('start_ip', None)
        self.end_ip = kwargs.get('end_ip', None)
        self.gateway = kwargs.get('gateway', None)
        self.netmask = kwargs.get('netmask', None)
        self.smb_server_fqdn = kwargs.get('smb_server_fqdn', None)
        self.provisioning_state = None
