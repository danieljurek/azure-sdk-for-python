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

from .resource import Resource


class ProximityPlacementGroup(Resource):
    """Specifies information about the proximity placement group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param proximity_placement_group_type: Specifies the type of the proximity
     placement group. <br><br> Possible values are: <br><br> **Standard**
     <br><br> **Ultra**. Possible values include: 'Standard', 'Ultra'
    :type proximity_placement_group_type: str or
     ~azure.mgmt.compute.v2018_06_01.models.ProximityPlacementGroupType
    :ivar virtual_machines: A list of references to all virtual machines in
     the proximity placement group.
    :vartype virtual_machines:
     list[~azure.mgmt.compute.v2018_06_01.models.SubResource]
    :ivar virtual_machine_scale_sets: A list of references to all virtual
     machine scale sets in the proximity placement group.
    :vartype virtual_machine_scale_sets:
     list[~azure.mgmt.compute.v2018_06_01.models.SubResource]
    :ivar availability_sets: A list of references to all availability sets in
     the proximity placement group.
    :vartype availability_sets:
     list[~azure.mgmt.compute.v2018_06_01.models.SubResource]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'virtual_machines': {'readonly': True},
        'virtual_machine_scale_sets': {'readonly': True},
        'availability_sets': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'proximity_placement_group_type': {'key': 'properties.proximityPlacementGroupType', 'type': 'str'},
        'virtual_machines': {'key': 'properties.virtualMachines', 'type': '[SubResource]'},
        'virtual_machine_scale_sets': {'key': 'properties.virtualMachineScaleSets', 'type': '[SubResource]'},
        'availability_sets': {'key': 'properties.availabilitySets', 'type': '[SubResource]'},
    }

    def __init__(self, **kwargs):
        super(ProximityPlacementGroup, self).__init__(**kwargs)
        self.proximity_placement_group_type = kwargs.get('proximity_placement_group_type', None)
        self.virtual_machines = None
        self.virtual_machine_scale_sets = None
        self.availability_sets = None
