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

from .proxy_resource_py3 import ProxyResource


class Job(ProxyResource):
    """Definition of the job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param runbook: Gets or sets the runbook.
    :type runbook: ~azure.mgmt.automation.models.RunbookAssociationProperty
    :param started_by: Gets or sets the job started by.
    :type started_by: str
    :param run_on: Gets or sets the runOn which specifies the group name where
     the job is to be executed.
    :type run_on: str
    :param job_id: Gets or sets the id of the job.
    :type job_id: str
    :param creation_time: Gets or sets the creation time of the job.
    :type creation_time: datetime
    :param status: Gets or sets the status of the job. Possible values
     include: 'New', 'Activating', 'Running', 'Completed', 'Failed', 'Stopped',
     'Blocked', 'Suspended', 'Disconnected', 'Suspending', 'Stopping',
     'Resuming', 'Removing'
    :type status: str or ~azure.mgmt.automation.models.JobStatus
    :param status_details: Gets or sets the status details of the job.
    :type status_details: str
    :param start_time: Gets or sets the start time of the job.
    :type start_time: datetime
    :param end_time: Gets or sets the end time of the job.
    :type end_time: datetime
    :param exception: Gets or sets the exception of the job.
    :type exception: str
    :param last_modified_time: Gets or sets the last modified time of the job.
    :type last_modified_time: datetime
    :param last_status_modified_time: Gets or sets the last status modified
     time of the job.
    :type last_status_modified_time: datetime
    :param parameters: Gets or sets the parameters of the job.
    :type parameters: dict[str, str]
    :param provisioning_state: The current provisioning state of the job.
     Possible values include: 'Failed', 'Succeeded', 'Suspended', 'Processing'
    :type provisioning_state: str or
     ~azure.mgmt.automation.models.JobProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'runbook': {'key': 'properties.runbook', 'type': 'RunbookAssociationProperty'},
        'started_by': {'key': 'properties.startedBy', 'type': 'str'},
        'run_on': {'key': 'properties.runOn', 'type': 'str'},
        'job_id': {'key': 'properties.jobId', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'status_details': {'key': 'properties.statusDetails', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'exception': {'key': 'properties.exception', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'last_status_modified_time': {'key': 'properties.lastStatusModifiedTime', 'type': 'iso-8601'},
        'parameters': {'key': 'properties.parameters', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, runbook=None, started_by: str=None, run_on: str=None, job_id: str=None, creation_time=None, status=None, status_details: str=None, start_time=None, end_time=None, exception: str=None, last_modified_time=None, last_status_modified_time=None, parameters=None, provisioning_state=None, **kwargs) -> None:
        super(Job, self).__init__(**kwargs)
        self.runbook = runbook
        self.started_by = started_by
        self.run_on = run_on
        self.job_id = job_id
        self.creation_time = creation_time
        self.status = status
        self.status_details = status_details
        self.start_time = start_time
        self.end_time = end_time
        self.exception = exception
        self.last_modified_time = last_modified_time
        self.last_status_modified_time = last_status_modified_time
        self.parameters = parameters
        self.provisioning_state = provisioning_state
