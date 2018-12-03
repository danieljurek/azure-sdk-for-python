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


class ProtectableContainer(Model):
    """Protectable Container Class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureStorageProtectableContainer,
    AzureVMAppContainerProtectableContainer

    All required parameters must be populated in order to send to Azure.

    :param friendly_name: Friendly name of the container.
    :type friendly_name: str
    :param backup_management_type: Type of backup management for the
     container. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param health_status: Status of health of the container.
    :type health_status: str
    :param container_id: Fabric Id of the container such as ARM Id.
    :type container_id: str
    :param protectable_container_type: Required. Constant filled by server.
    :type protectable_container_type: str
    """

    _validation = {
        'protectable_container_type': {'required': True},
    }

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'health_status': {'key': 'healthStatus', 'type': 'str'},
        'container_id': {'key': 'containerId', 'type': 'str'},
        'protectable_container_type': {'key': 'protectableContainerType', 'type': 'str'},
    }

    _subtype_map = {
        'protectable_container_type': {'StorageContainer': 'AzureStorageProtectableContainer', 'VMAppContainer': 'AzureVMAppContainerProtectableContainer'}
    }

    def __init__(self, **kwargs):
        super(ProtectableContainer, self).__init__(**kwargs)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.backup_management_type = kwargs.get('backup_management_type', None)
        self.health_status = kwargs.get('health_status', None)
        self.container_id = kwargs.get('container_id', None)
        self.protectable_container_type = None
