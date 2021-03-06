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


class AzureIaaSVMJobExtendedInfo(Model):
    """Azure IaaS VM workload-specific additional information for job.

    :param tasks_list: List of tasks associated with this job.
    :type tasks_list:
     list[~azure.mgmt.recoveryservicesbackup.models.AzureIaaSVMJobTaskDetails]
    :param property_bag: Job properties.
    :type property_bag: dict[str, str]
    :param internal_property_bag: Job internal properties.
    :type internal_property_bag: dict[str, str]
    :param progress_percentage: Indicates progress of the job. Null if it has
     not started or completed.
    :type progress_percentage: float
    :param estimated_remaining_duration: Time remaining for execution of this
     job.
    :type estimated_remaining_duration: str
    :param dynamic_error_message: Non localized error message on job
     execution.
    :type dynamic_error_message: str
    """

    _attribute_map = {
        'tasks_list': {'key': 'tasksList', 'type': '[AzureIaaSVMJobTaskDetails]'},
        'property_bag': {'key': 'propertyBag', 'type': '{str}'},
        'internal_property_bag': {'key': 'internalPropertyBag', 'type': '{str}'},
        'progress_percentage': {'key': 'progressPercentage', 'type': 'float'},
        'estimated_remaining_duration': {'key': 'estimatedRemainingDuration', 'type': 'str'},
        'dynamic_error_message': {'key': 'dynamicErrorMessage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureIaaSVMJobExtendedInfo, self).__init__(**kwargs)
        self.tasks_list = kwargs.get('tasks_list', None)
        self.property_bag = kwargs.get('property_bag', None)
        self.internal_property_bag = kwargs.get('internal_property_bag', None)
        self.progress_percentage = kwargs.get('progress_percentage', None)
        self.estimated_remaining_duration = kwargs.get('estimated_remaining_duration', None)
        self.dynamic_error_message = kwargs.get('dynamic_error_message', None)
