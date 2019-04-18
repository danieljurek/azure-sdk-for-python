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


class OperationDefinitionDisplay(Model):
    """The display information for a configuration store operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: The resource provider name: Microsoft App Configuration."
    :vartype provider: str
    :param resource: The resource on which the operation is performed.
    :type resource: str
    :param operation: The operation that users can perform.
    :type operation: str
    :param description: The description for the operation.
    :type description: str
    """

    _validation = {
        'provider': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(OperationDefinitionDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = resource
        self.operation = operation
        self.description = description
