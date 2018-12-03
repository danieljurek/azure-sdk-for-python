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

from .workload_protectable_item_py3 import WorkloadProtectableItem


class AzureFileShareProtectableItem(WorkloadProtectableItem):
    """Protectable item for Azure Fileshare workloads.

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup management to backup an
     item.
    :type backup_management_type: str
    :param workload_type: Type of workload for the backup management
    :type workload_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param protectable_item_type: Required. Constant filled by server.
    :type protectable_item_type: str
    :param parent_container_fabric_id: Full Fabric ID of container to which
     this protectable item belongs. For example, ARM ID.
    :type parent_container_fabric_id: str
    :param parent_container_friendly_name: Friendly name of container to which
     this protectable item belongs.
    :type parent_container_friendly_name: str
    :param azure_file_share_type: File Share type XSync or XSMB. Possible
     values include: 'Invalid', 'XSMB', 'XSync'
    :type azure_file_share_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.AzureFileShareType
    """

    _validation = {
        'protectable_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'protectable_item_type': {'key': 'protectableItemType', 'type': 'str'},
        'parent_container_fabric_id': {'key': 'parentContainerFabricId', 'type': 'str'},
        'parent_container_friendly_name': {'key': 'parentContainerFriendlyName', 'type': 'str'},
        'azure_file_share_type': {'key': 'azureFileShareType', 'type': 'str'},
    }

    def __init__(self, *, backup_management_type: str=None, workload_type: str=None, friendly_name: str=None, protection_state=None, parent_container_fabric_id: str=None, parent_container_friendly_name: str=None, azure_file_share_type=None, **kwargs) -> None:
        super(AzureFileShareProtectableItem, self).__init__(backup_management_type=backup_management_type, workload_type=workload_type, friendly_name=friendly_name, protection_state=protection_state, **kwargs)
        self.parent_container_fabric_id = parent_container_fabric_id
        self.parent_container_friendly_name = parent_container_friendly_name
        self.azure_file_share_type = azure_file_share_type
        self.protectable_item_type = 'AzureFileShare'
