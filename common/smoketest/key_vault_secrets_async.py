# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
import uuid
from azure.keyvault.secrets.aio import SecretClient
from key_vault_base_async import KeyVaultBaseAsync


class KeyVaultSecrets(KeyVaultBaseAsync):
    def __init__(self):
        credential = self.get_default_credential(os.environ.get('AZURE_AUTHORITY_HOST_ALIAS'))
        self.secret_client = SecretClient(
            vault_url=os.environ["AZURE_PROJECT_URL"], credential=credential
        )
        self.secret_name = "secret-name-" + uuid.uuid1().hex
        self.secret_value = "secret-value"

    async def set_secret(self):
        print("Setting a secret...")
        secret = await self.secret_client.set_secret(
            self.secret_name, self.secret_value
        )
        print("\tdone, secret: (" + secret.name + "," + secret.value + ").")

    async def get_secret(self):
        print("Getting a secret...")
        secret = await self.secret_client.get_secret(self.secret_name)
        print("\tdone, secret: (" + secret.name + "," + secret.value + ").")

    async def delete_secret(self):
        print("Deleting a secret...")
        await self.secret_client.delete_secret(self.secret_name)
        print("\tdone")

    async def run(self):

        print("")
        print("------------------------")
        print("Key Vault - Secrets\nIdentity - Credential")
        print("------------------------")
        print("1) Set a secret")
        print("2) Get that secret")
        print("3) Delete that secret (Clean up the resource)")
        print("")

        try:
            await self.set_secret()
            await self.get_secret()
        finally:
            await self.delete_secret()
