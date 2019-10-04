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


class KeyVaultSecretStatus(str, Enum):

    initialized = "Initialized"
    waiting_on_certificate_order = "WaitingOnCertificateOrder"
    succeeded = "Succeeded"
    certificate_order_failed = "CertificateOrderFailed"
    operation_not_permitted_on_key_vault = "OperationNotPermittedOnKeyVault"
    azure_service_unauthorized_to_access_key_vault = "AzureServiceUnauthorizedToAccessKeyVault"
    key_vault_does_not_exist = "KeyVaultDoesNotExist"
    key_vault_secret_does_not_exist = "KeyVaultSecretDoesNotExist"
    unknown_error = "UnknownError"
    external_private_key = "ExternalPrivateKey"
    unknown = "Unknown"


class RouteType(str, Enum):

    default = "DEFAULT"
    inherited = "INHERITED"
    static = "STATIC"


class ManagedServiceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"


class IpFilterTag(str, Enum):

    default = "Default"
    xff_proxy = "XffProxy"


class AutoHealActionType(str, Enum):

    recycle = "Recycle"
    log_event = "LogEvent"
    custom_action = "CustomAction"


class ConnectionStringType(str, Enum):

    my_sql = "MySql"
    sql_server = "SQLServer"
    sql_azure = "SQLAzure"
    custom = "Custom"
    notification_hub = "NotificationHub"
    service_bus = "ServiceBus"
    event_hub = "EventHub"
    api_hub = "ApiHub"
    doc_db = "DocDb"
    redis_cache = "RedisCache"
    postgre_sql = "PostgreSQL"


class AzureStorageType(str, Enum):

    azure_files = "AzureFiles"
    azure_blob = "AzureBlob"


class AzureStorageState(str, Enum):

    ok = "Ok"
    invalid_credentials = "InvalidCredentials"
    invalid_share = "InvalidShare"


class ScmType(str, Enum):

    none = "None"
    dropbox = "Dropbox"
    tfs = "Tfs"
    local_git = "LocalGit"
    git_hub = "GitHub"
    code_plex_git = "CodePlexGit"
    code_plex_hg = "CodePlexHg"
    bitbucket_git = "BitbucketGit"
    bitbucket_hg = "BitbucketHg"
    external_git = "ExternalGit"
    external_hg = "ExternalHg"
    one_drive = "OneDrive"
    vso = "VSO"


class ManagedPipelineMode(str, Enum):

    integrated = "Integrated"
    classic = "Classic"


class SiteLoadBalancing(str, Enum):

    weighted_round_robin = "WeightedRoundRobin"
    least_requests = "LeastRequests"
    least_response_time = "LeastResponseTime"
    weighted_total_traffic = "WeightedTotalTraffic"
    request_hash = "RequestHash"


class SupportedTlsVersions(str, Enum):

    one_full_stop_zero = "1.0"
    one_full_stop_one = "1.1"
    one_full_stop_two = "1.2"


class FtpsState(str, Enum):

    all_allowed = "AllAllowed"
    ftps_only = "FtpsOnly"
    disabled = "Disabled"


class SslState(str, Enum):

    disabled = "Disabled"
    sni_enabled = "SniEnabled"
    ip_based_enabled = "IpBasedEnabled"


class HostType(str, Enum):

    standard = "Standard"
    repository = "Repository"


class UsageState(str, Enum):

    normal = "Normal"
    exceeded = "Exceeded"


class SiteAvailabilityState(str, Enum):

    normal = "Normal"
    limited = "Limited"
    disaster_recovery_mode = "DisasterRecoveryMode"


class RedundancyMode(str, Enum):

    none = "None"
    manual = "Manual"
    failover = "Failover"
    active_active = "ActiveActive"
    geo_redundant = "GeoRedundant"


class StatusOptions(str, Enum):

    ready = "Ready"
    pending = "Pending"
    creating = "Creating"


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    in_progress = "InProgress"
    deleting = "Deleting"
