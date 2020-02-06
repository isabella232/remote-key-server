# Software Name : Remote Key Server
# Version: 0.9.0
# SPDX-FileCopyrightText: Copyright (c) 2020 Orange
# SPDX-License-Identifier: MPL-2.0
#
# This software is distributed under the Mozilla Public License 2.0,
# the text of which is available at https://www.mozilla.org/en-US/MPL/2.0/
# or see the "LICENSE" file for more details.
#
# Author: Glenn Feunteun, Celine Nicolas
# coding: utf-8

"""
    Remote Key Server API

    Describes RKS API  # noqa: E501

    OpenAPI spec version: 0.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import pytest

import rks
from rks.api.rks_secrets_api import RKSSecretsApi  # noqa: E501
from rks.rest import ApiException

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class TestRKSSecretsApi(object):
    """RKSSecretsApi unit test stubs"""

    def test_get_secret(
        self, secret_api, node_token, test_dot_com_secret, associate_dot_com_group
    ):
        secret_api.api_client.configuration.api_key["X-Vault-Token"] = node_token
        secret = secret_api.get_secret("test.com")
        print(secret)
        assert secret.data != None
        assert secret.data.certificate != None
        assert secret.data.private_key != None
        assert secret.data.meta != None


if __name__ == "__main__":
    pytest.main()
