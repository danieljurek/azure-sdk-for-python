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

from .protected_item import ProtectedItem


class AzureFileshareProtectedItem(ProtectedItem):
    """Azure File Share workload-specific backup item.

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup management for the backed up
     item. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param workload_type: Type of workload this item represents. Possible
     values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB',
     'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource', 'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase'
    :type workload_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.DataSourceType
    :param container_name: Unique name of container
    :type container_name: str
    :param source_resource_id: ARM ID of the resource to be backed up.
    :type source_resource_id: str
    :param policy_id: ID of the backup policy with which this item is backed
     up.
    :type policy_id: str
    :param last_recovery_point: Timestamp when the last (latest) backup copy
     was created for this backup item.
    :type last_recovery_point: datetime
    :param backup_set_name: Name of the backup set the backup item belongs to
    :type backup_set_name: str
    :param create_mode: Create mode to indicate recovery of existing soft
     deleted data source or creation of new data source. Possible values
     include: 'Invalid', 'Default', 'Recover'
    :type create_mode: str or
     ~azure.mgmt.recoveryservicesbackup.models.CreateMode
    :param protected_item_type: Required. Constant filled by server.
    :type protected_item_type: str
    :param friendly_name: Friendly name of the fileshare represented by this
     backup item.
    :type friendly_name: str
    :param protection_status: Backup status of this backup item.
    :type protection_status: str
    :param protection_state: Backup state of this backup item. Possible values
     include: 'Invalid', 'IRPending', 'Protected', 'ProtectionError',
     'ProtectionStopped', 'ProtectionPaused'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionState
    :param health_status: backups running status for this backup item.
     Possible values include: 'Passed', 'ActionRequired', 'ActionSuggested',
     'Invalid'
    :type health_status: str or
     ~azure.mgmt.recoveryservicesbackup.models.HealthStatus
    :param last_backup_status: Last backup operation status. Possible values:
     Healthy, Unhealthy.
    :type last_backup_status: str
    :param last_backup_time: Timestamp of the last backup operation on this
     backup item.
    :type last_backup_time: datetime
    :param extended_info: Additional information with this backup item.
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.AzureFileshareProtectedItemExtendedInfo
    """

    _validation = {
        'protected_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'policy_id': {'key': 'policyId', 'type': 'str'},
        'last_recovery_point': {'key': 'lastRecoveryPoint', 'type': 'iso-8601'},
        'backup_set_name': {'key': 'backupSetName', 'type': 'str'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'protected_item_type': {'key': 'protectedItemType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_status': {'key': 'protectionStatus', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'health_status': {'key': 'healthStatus', 'type': 'str'},
        'last_backup_status': {'key': 'lastBackupStatus', 'type': 'str'},
        'last_backup_time': {'key': 'lastBackupTime', 'type': 'iso-8601'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AzureFileshareProtectedItemExtendedInfo'},
    }

    def __init__(self, **kwargs):
        super(AzureFileshareProtectedItem, self).__init__(**kwargs)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.protection_status = kwargs.get('protection_status', None)
        self.protection_state = kwargs.get('protection_state', None)
        self.health_status = kwargs.get('health_status', None)
        self.last_backup_status = kwargs.get('last_backup_status', None)
        self.last_backup_time = kwargs.get('last_backup_time', None)
        self.extended_info = kwargs.get('extended_info', None)
        self.protected_item_type = 'AzureFileShareProtectedItem'
