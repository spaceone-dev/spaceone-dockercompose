import os
import uuid
import unittest
import random

from langcodes import Language

from spaceone.core.utils import random_string
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core.pygrpc.message_type import *

from spaceone.tester import TestCase, print_json

aws_access_key = {
    'name': 'aws_access_key',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'aws_access_key_id',
            'aws_secret_access_key'
        ],
        'properties': {
            'aws_access_key_id': {
                'title': 'AWS Access Key',
                'type': 'string',
                'minLength': 4
            },
            'region_name': {
                'title': 'Region',
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'ap-northeast-2'
                ]
            },
            'aws_secret_access_key': {
                'type': 'string',
                'minLength': 4,
                'title': 'AWS Secret Key'
            }
        },
        'type': 'object'
    },
    'labels': ['AWS'],
    'tags': {
        'description': 'AWS Access Key'
    }
}
aws_assume_role = {
    'name': 'aws_assume_role',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'aws_access_key_id',
            'aws_secret_access_key',
            'role_arn'
        ],
        'properties': {
            'role_arn': {
                'title': 'Role ARN',
                'type': 'string',
                'minLength': 4
            },
            'aws_access_key_id': {
                'title': 'AWS Access Key',
                'type': 'string',
                'minLength': 4
            },
            'region_name': {
                'title': 'Region',
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'ap-northeast-2'
                ]
            },
            'aws_secret_access_key': {
                'type': 'string',
                'minLength': 4,
                'title': 'AWS Secret Key'
            }
        },
        'type': 'object'
    },
    'labels': ['AWS', 'Assume Role'],
    'tags': {
        'description': 'AWS Assume Role'
    }
}
google_api_key = {
    'name': 'google_api_key',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'api_key'
        ],
        'properties': {
            'api_key': {
                'title': 'API Key',
                'type': 'string',
                'minLength': 4
            }
        },
        'type': 'object'
    },
    'labels': ['Google Cloud', 'GCP'],
    'tags': {
        'description': 'Google API Key'
    }
}
google_oauth_client_id = {
    'name': 'google_oauth_client_id',
    'service_type': 'secret.credentials',
    'schema': {
        'properties': {
            'auth_provider_x509_cert_url': {
                'title': 'Auth Provider Cert URL',
                'type': 'string',
                'minLength': 4,
                'default': 'https://www.googleapis.com/oauth2/v1/certs'
            },
            'client_id': {
                'title': 'Client ID',
                'type': 'string',
                'minLength': 4,
                'examples': [
                    '10118252.....'
                ]
            },
            'token_uri': {
                'type': 'string',
                'minLength': 4,
                'default': 'https://oauth2.googleapis.com/token',
                'title': 'Token URI'
            },
            'zone': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'asia-northeast3'
                ],
                'title': 'Region'
            },
            'client_x509_cert_url': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'https://www.googleapis.com/...'
                ],
                'title': 'client_x509_cert_url'
            },
            'project_id': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'project-id'
                ],
                'title': 'Project ID'
            },
            'private_key_id': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    '771823abcd...'
                ],
                'title': 'Private Key ID'
            },
            'auth_uri': {
                'type': 'string',
                'minLength': 4,
                'default': 'https://acounts.google.com/o/oauth2/auth',
                'title': 'Auth URI'
            },
            'type': {
                'default': 'service_account',
                'title': 'Type',
                'type': 'string',
                'minLength': 4
            },
            'client_email': {
                'type': 'string',
                'minLength': 4,
                'exmaples': [
                    '<api-name>api@project-id.iam.gserviceaccount.com(opens in new tab)'
                ],
                'title': 'Client Email'
            },
            'private_key': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    '-----BEGIN'
                ],
                'title': 'Private Key'
            }
        },
        'type': 'object',
        'required': [
            'type',
            'project_id',
            'private_key_id',
            'private_key',
            'client_email',
            'client_id',
            'auth_uri',
            'token_uri',
            'auth_provider_x509_cert_url',
            'client_x509_cert_url'
        ]
    },
    'labels': ['Google Cloud', 'GCP', 'OAuth2.0'],
    'tags': {
        'description': 'Google OAuth Client ID'
    }
}
azure_client_secret = {
    'name': 'azure_client_secret',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'client_id',
            'client_secret',
            'tenant_id',
            'subscription_id'
        ],
        'properties': {
            'client_id': {
                'title': 'Client ID',
                'type': 'string',
                'minLength': 4
            },
            'client_secret': {
                'title': 'Client Secret',
                'type': 'string',
                'minLength': 4
            },
            'tenant_id': {
                'title': 'Tenant ID',
                'type': 'string',
                'minLength': 4
            },
            'subscription_id': {
                'title': 'Subscription ID',
                'type': 'string',
                'minLength': 4
            }
        },
        'type': 'object'
    },
    'labels': ['Azure'],
    'tags': {
        'description': 'Azure Client Secret'
    }
}

SCHEMA_PARAMS = {
    'aws_acess_key': aws_access_key,
    'aws_assume_role': aws_assume_role,
    'google_api_key': google_api_key,
    'google_oauth_client_id': google_oauth_client_id,
    'azure_client_secret': azure_client_secret
}


class TestRepository(TestCase):

    def _create_schema(self, params):
        """" Create repository.Schema based on params

        """
        params.update({'domain_id': self.domain.domain_id})
        schema = self.repository.Schema.create(params, metadata=self.meta)
        print_json(schema)

        return schema

    def test_create(self):
        for key, schema_param in SCHEMA_PARAMS.items():
            self._create_schema(schema_param)

if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
