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


class ImageTemplateIdentity(Model):
    """Identity for the image template.

    :param type: The type of identity used for the image template. The type
     'None' will remove any identities from the image template. Possible values
     include: 'UserAssigned', 'None'
    :type type: str or ~azure.mgmt.imagebuilder.models.ResourceIdentityType
    :param user_assigned_identities: The list of user identities associated
     with the image template. The user identity dictionary key references will
     be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    :type user_assigned_identities: dict[str,
     ~azure.mgmt.imagebuilder.models.ImageTemplateIdentityUserAssignedIdentitiesValue]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{ImageTemplateIdentityUserAssignedIdentitiesValue}'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateIdentity, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.user_assigned_identities = kwargs.get('user_assigned_identities', None)
