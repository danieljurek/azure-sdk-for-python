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

from enum import Enum


class CheckNameAvailabilityReason(str, Enum):

    invalid = "Invalid"
    already_exists = "AlreadyExists"


class ServerConnectionType(str, Enum):

    default = "Default"
    proxy = "Proxy"
    redirect = "Redirect"


class SecurityAlertPolicyState(str, Enum):

    new = "New"
    enabled = "Enabled"
    disabled = "Disabled"


class SecurityAlertPolicyEmailAccountAdmins(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class SecurityAlertPolicyUseServerDefault(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class DataMaskingState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class DataMaskingRuleState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class DataMaskingFunction(str, Enum):

    default = "Default"
    ccn = "CCN"
    email = "Email"
    number = "Number"
    ssn = "SSN"
    text = "Text"


class GeoBackupPolicyState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class DatabaseEdition(str, Enum):

    web = "Web"
    business = "Business"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"
    free = "Free"
    stretch = "Stretch"
    data_warehouse = "DataWarehouse"
    system = "System"
    system2 = "System2"
    general_purpose = "GeneralPurpose"
    business_critical = "BusinessCritical"
    hyperscale = "Hyperscale"


class ServiceObjectiveName(str, Enum):

    system = "System"
    system0 = "System0"
    system1 = "System1"
    system2 = "System2"
    system3 = "System3"
    system4 = "System4"
    system2_l = "System2L"
    system3_l = "System3L"
    system4_l = "System4L"
    free = "Free"
    basic = "Basic"
    s0 = "S0"
    s1 = "S1"
    s2 = "S2"
    s3 = "S3"
    s4 = "S4"
    s6 = "S6"
    s7 = "S7"
    s9 = "S9"
    s12 = "S12"
    p1 = "P1"
    p2 = "P2"
    p3 = "P3"
    p4 = "P4"
    p6 = "P6"
    p11 = "P11"
    p15 = "P15"
    prs1 = "PRS1"
    prs2 = "PRS2"
    prs4 = "PRS4"
    prs6 = "PRS6"
    dw100 = "DW100"
    dw200 = "DW200"
    dw300 = "DW300"
    dw400 = "DW400"
    dw500 = "DW500"
    dw600 = "DW600"
    dw1000 = "DW1000"
    dw1200 = "DW1200"
    dw1000c = "DW1000c"
    dw1500 = "DW1500"
    dw1500c = "DW1500c"
    dw2000 = "DW2000"
    dw2000c = "DW2000c"
    dw3000 = "DW3000"
    dw2500c = "DW2500c"
    dw3000c = "DW3000c"
    dw6000 = "DW6000"
    dw5000c = "DW5000c"
    dw6000c = "DW6000c"
    dw7500c = "DW7500c"
    dw10000c = "DW10000c"
    dw15000c = "DW15000c"
    dw30000c = "DW30000c"
    ds100 = "DS100"
    ds200 = "DS200"
    ds300 = "DS300"
    ds400 = "DS400"
    ds500 = "DS500"
    ds600 = "DS600"
    ds1000 = "DS1000"
    ds1200 = "DS1200"
    ds1500 = "DS1500"
    ds2000 = "DS2000"
    elastic_pool = "ElasticPool"


class StorageKeyType(str, Enum):

    storage_access_key = "StorageAccessKey"
    shared_access_key = "SharedAccessKey"


class AuthenticationType(str, Enum):

    sql = "SQL"
    ad_password = "ADPassword"


class UnitType(str, Enum):

    count = "count"
    bytes = "bytes"
    seconds = "seconds"
    percent = "percent"
    count_per_second = "countPerSecond"
    bytes_per_second = "bytesPerSecond"


class PrimaryAggregationType(str, Enum):

    none = "None"
    average = "Average"
    count = "Count"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"


class UnitDefinitionType(str, Enum):

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    count_per_second = "CountPerSecond"
    bytes_per_second = "BytesPerSecond"


class ElasticPoolEdition(str, Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    general_purpose = "GeneralPurpose"
    business_critical = "BusinessCritical"


class ReplicationRole(str, Enum):

    primary = "Primary"
    secondary = "Secondary"
    non_readable_secondary = "NonReadableSecondary"
    source = "Source"
    copy = "Copy"


class ReplicationState(str, Enum):

    pending = "PENDING"
    seeding = "SEEDING"
    catch_up = "CATCH_UP"
    suspended = "SUSPENDED"


class RecommendedIndexAction(str, Enum):

    create = "Create"
    drop = "Drop"
    rebuild = "Rebuild"


class RecommendedIndexState(str, Enum):

    active = "Active"
    pending = "Pending"
    executing = "Executing"
    verifying = "Verifying"
    pending_revert = "Pending Revert"
    reverting = "Reverting"
    reverted = "Reverted"
    ignored = "Ignored"
    expired = "Expired"
    blocked = "Blocked"
    success = "Success"


class RecommendedIndexType(str, Enum):

    clustered = "CLUSTERED"
    nonclustered = "NONCLUSTERED"
    columnstore = "COLUMNSTORE"
    clusteredcolumnstore = "CLUSTERED COLUMNSTORE"


class TransparentDataEncryptionStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class TransparentDataEncryptionActivityStatus(str, Enum):

    encrypting = "Encrypting"
    decrypting = "Decrypting"


class AutomaticTuningMode(str, Enum):

    inherit = "Inherit"
    custom = "Custom"
    auto = "Auto"
    unspecified = "Unspecified"


class AutomaticTuningOptionModeDesired(str, Enum):

    off = "Off"
    on = "On"
    default = "Default"


class AutomaticTuningOptionModeActual(str, Enum):

    off = "Off"
    on = "On"


class AutomaticTuningDisabledReason(str, Enum):

    default = "Default"
    disabled = "Disabled"
    auto_configured = "AutoConfigured"
    inherited_from_server = "InheritedFromServer"
    query_store_off = "QueryStoreOff"
    query_store_read_only = "QueryStoreReadOnly"
    not_supported = "NotSupported"


class ServerKeyType(str, Enum):

    service_managed = "ServiceManaged"
    azure_key_vault = "AzureKeyVault"


class ReadWriteEndpointFailoverPolicy(str, Enum):

    manual = "Manual"
    automatic = "Automatic"


class ReadOnlyEndpointFailoverPolicy(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class FailoverGroupReplicationRole(str, Enum):

    primary = "Primary"
    secondary = "Secondary"


class OperationOrigin(str, Enum):

    user = "user"
    system = "system"


class IdentityType(str, Enum):

    system_assigned = "SystemAssigned"


class SyncAgentState(str, Enum):

    online = "Online"
    offline = "Offline"
    never_connected = "NeverConnected"


class SyncMemberDbType(str, Enum):

    azure_sql_database = "AzureSqlDatabase"
    sql_server_database = "SqlServerDatabase"


class SyncGroupLogType(str, Enum):

    all = "All"
    error = "Error"
    warning = "Warning"
    success = "Success"


class SyncConflictResolutionPolicy(str, Enum):

    hub_win = "HubWin"
    member_win = "MemberWin"


class SyncGroupState(str, Enum):

    not_ready = "NotReady"
    error = "Error"
    warning = "Warning"
    progressing = "Progressing"
    good = "Good"


class SyncDirection(str, Enum):

    bidirectional = "Bidirectional"
    one_way_member_to_hub = "OneWayMemberToHub"
    one_way_hub_to_member = "OneWayHubToMember"


class SyncMemberState(str, Enum):

    sync_in_progress = "SyncInProgress"
    sync_succeeded = "SyncSucceeded"
    sync_failed = "SyncFailed"
    disabled_tombstone_cleanup = "DisabledTombstoneCleanup"
    disabled_backup_restore = "DisabledBackupRestore"
    sync_succeeded_with_warnings = "SyncSucceededWithWarnings"
    sync_cancelling = "SyncCancelling"
    sync_cancelled = "SyncCancelled"
    un_provisioned = "UnProvisioned"
    provisioning = "Provisioning"
    provisioned = "Provisioned"
    provision_failed = "ProvisionFailed"
    de_provisioning = "DeProvisioning"
    de_provisioned = "DeProvisioned"
    de_provision_failed = "DeProvisionFailed"
    reprovisioning = "Reprovisioning"
    reprovision_failed = "ReprovisionFailed"
    un_reprovisioned = "UnReprovisioned"


class VirtualNetworkRuleState(str, Enum):

    initializing = "Initializing"
    in_progress = "InProgress"
    ready = "Ready"
    deleting = "Deleting"
    unknown = "Unknown"


class BlobAuditingPolicyState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class JobAgentState(str, Enum):

    creating = "Creating"
    ready = "Ready"
    updating = "Updating"
    deleting = "Deleting"
    disabled = "Disabled"


class JobExecutionLifecycle(str, Enum):

    created = "Created"
    in_progress = "InProgress"
    waiting_for_child_job_executions = "WaitingForChildJobExecutions"
    waiting_for_retry = "WaitingForRetry"
    succeeded = "Succeeded"
    succeeded_with_skipped = "SucceededWithSkipped"
    failed = "Failed"
    timed_out = "TimedOut"
    canceled = "Canceled"
    skipped = "Skipped"


class ProvisioningState(str, Enum):

    created = "Created"
    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"


class JobTargetType(str, Enum):

    target_group = "TargetGroup"
    sql_database = "SqlDatabase"
    sql_elastic_pool = "SqlElasticPool"
    sql_shard_map = "SqlShardMap"
    sql_server = "SqlServer"


class JobScheduleType(str, Enum):

    once = "Once"
    recurring = "Recurring"


class JobStepActionType(str, Enum):

    tsql = "TSql"


class JobStepActionSource(str, Enum):

    inline = "Inline"


class JobStepOutputType(str, Enum):

    sql_database = "SqlDatabase"


class JobTargetGroupMembershipType(str, Enum):

    include = "Include"
    exclude = "Exclude"


class AutomaticTuningServerMode(str, Enum):

    custom = "Custom"
    auto = "Auto"
    unspecified = "Unspecified"


class AutomaticTuningServerReason(str, Enum):

    default = "Default"
    disabled = "Disabled"
    auto_configured = "AutoConfigured"


class RestorePointType(str, Enum):

    continuous = "CONTINUOUS"
    discrete = "DISCRETE"


class ManagementOperationState(str, Enum):

    pending = "Pending"
    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
    cancel_in_progress = "CancelInProgress"
    cancelled = "Cancelled"


class MaxSizeUnit(str, Enum):

    megabytes = "Megabytes"
    gigabytes = "Gigabytes"
    terabytes = "Terabytes"
    petabytes = "Petabytes"


class LogSizeUnit(str, Enum):

    megabytes = "Megabytes"
    gigabytes = "Gigabytes"
    terabytes = "Terabytes"
    petabytes = "Petabytes"
    percent = "Percent"


class CapabilityStatus(str, Enum):

    visible = "Visible"
    available = "Available"
    default = "Default"
    disabled = "Disabled"


class PerformanceLevelUnit(str, Enum):

    dtu = "DTU"
    vcores = "VCores"


class CreateMode(str, Enum):

    default = "Default"
    copy = "Copy"
    secondary = "Secondary"
    point_in_time_restore = "PointInTimeRestore"
    restore = "Restore"
    recovery = "Recovery"
    restore_external_backup = "RestoreExternalBackup"
    restore_external_backup_secondary = "RestoreExternalBackupSecondary"
    restore_long_term_retention_backup = "RestoreLongTermRetentionBackup"
    online_secondary = "OnlineSecondary"


class SampleName(str, Enum):

    adventure_works_lt = "AdventureWorksLT"
    wide_world_importers_std = "WideWorldImportersStd"
    wide_world_importers_full = "WideWorldImportersFull"


class DatabaseStatus(str, Enum):

    online = "Online"
    restoring = "Restoring"
    recovery_pending = "RecoveryPending"
    recovering = "Recovering"
    suspect = "Suspect"
    offline = "Offline"
    standby = "Standby"
    shutdown = "Shutdown"
    emergency_mode = "EmergencyMode"
    auto_closed = "AutoClosed"
    copying = "Copying"
    creating = "Creating"
    inaccessible = "Inaccessible"
    offline_secondary = "OfflineSecondary"
    pausing = "Pausing"
    paused = "Paused"
    resuming = "Resuming"
    scaling = "Scaling"
    offline_changing_dw_performance_tiers = "OfflineChangingDwPerformanceTiers"
    online_changing_dw_performance_tiers = "OnlineChangingDwPerformanceTiers"
    disabled = "Disabled"


class CatalogCollationType(str, Enum):

    database_default = "DATABASE_DEFAULT"
    sql_latin1_general_cp1_ci_as = "SQL_Latin1_General_CP1_CI_AS"


class DatabaseLicenseType(str, Enum):

    license_included = "LicenseIncluded"
    base_price = "BasePrice"


class DatabaseReadScale(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ElasticPoolState(str, Enum):

    creating = "Creating"
    ready = "Ready"
    disabled = "Disabled"


class ElasticPoolLicenseType(str, Enum):

    license_included = "LicenseIncluded"
    base_price = "BasePrice"


class VulnerabilityAssessmentScanTriggerType(str, Enum):

    on_demand = "OnDemand"
    recurring = "Recurring"


class VulnerabilityAssessmentScanState(str, Enum):

    passed = "Passed"
    failed = "Failed"
    failed_to_run = "FailedToRun"
    in_progress = "InProgress"


class InstanceFailoverGroupReplicationRole(str, Enum):

    primary = "Primary"
    secondary = "Secondary"


class InstancePoolLicenseType(str, Enum):

    license_included = "LicenseIncluded"
    base_price = "BasePrice"


class ManagedServerCreateMode(str, Enum):

    default = "Default"
    point_in_time_restore = "PointInTimeRestore"


class ManagedInstanceLicenseType(str, Enum):

    license_included = "LicenseIncluded"
    base_price = "BasePrice"


class ManagedInstanceProxyOverride(str, Enum):

    proxy = "Proxy"
    redirect = "Redirect"
    default = "Default"


class ManagedDatabaseStatus(str, Enum):

    online = "Online"
    offline = "Offline"
    shutdown = "Shutdown"
    creating = "Creating"
    inaccessible = "Inaccessible"
    restoring = "Restoring"
    updating = "Updating"


class ManagedDatabaseCreateMode(str, Enum):

    default = "Default"
    restore_external_backup = "RestoreExternalBackup"
    point_in_time_restore = "PointInTimeRestore"
    recovery = "Recovery"


class LongTermRetentionDatabaseState(str, Enum):

    all = "All"
    live = "Live"
    deleted = "Deleted"


class VulnerabilityAssessmentPolicyBaselineName(str, Enum):

    master = "master"
    default = "default"


class SensitivityLabelSource(str, Enum):

    current = "current"
    recommended = "recommended"


class CapabilityGroup(str, Enum):

    supported_editions = "supportedEditions"
    supported_elastic_pool_editions = "supportedElasticPoolEditions"
    supported_managed_instance_versions = "supportedManagedInstanceVersions"
