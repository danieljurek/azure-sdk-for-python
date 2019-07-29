# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import unittest
import pytest
import asyncio

from azure.storage.blob.aio import BlobServiceClient

from testcase import (
    StorageTestCase,
    TestMode
)

SERVICE_UNAVAILABLE_RESP_BODY = '<?xml version="1.0" encoding="utf-8"?><StorageServiceStats><GeoReplication><Status' \
                                '>unavailable</Status><LastSyncTime></LastSyncTime></GeoReplication' \
                                '></StorageServiceStats> '


# --Test Class -----------------------------------------------------------------
class ServiceStatsTestAsync(StorageTestCase):
    # --Helpers-----------------------------------------------------------------
    def _assert_stats_default(self, stats):
        self.assertIsNotNone(stats)
        self.assertIsNotNone(stats.geo_replication)

        self.assertEqual(stats.geo_replication.status, 'live')
        self.assertIsNotNone(stats.geo_replication.last_sync_time)

    def _assert_stats_unavailable(self, stats):
        self.assertIsNotNone(stats)
        self.assertIsNotNone(stats.geo_replication)

        self.assertEqual(stats.geo_replication.status, 'unavailable')
        self.assertIsNone(stats.geo_replication.last_sync_time)

    @staticmethod
    def override_response_body_with_unavailable_status(response):
        response.http_response.text = lambda: SERVICE_UNAVAILABLE_RESP_BODY

    # --Test cases per service ---------------------------------------

    async def _test_blob_service_stats_async(self):
        # Arrange
        url = self._get_account_url()
        credential = self._get_shared_key_credential()
        bs = BlobServiceClient(url, credential=credential)
        # Act
        stats = await bs.get_service_stats()

        # Assert
        self._assert_stats_default(stats)

    def test_blob_service_stats_async(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_blob_service_stats_async())

    async def _test_blob_service_stats_when_unavailable_async(self):
        # Arrange
        url = self._get_account_url()
        credential = self._get_shared_key_credential()
        bs = BlobServiceClient(url, credential=credential)

        # Act
        stats = await bs.get_service_stats(raw_response_hook=self.override_response_body_with_unavailable_status)

        # Assert
        self._assert_stats_unavailable(stats)

    def test_blob_service_stats_when_unavailable_async(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_blob_service_stats_when_unavailable_async())

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
