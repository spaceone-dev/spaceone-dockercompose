import os
import uuid
import unittest
import random

from langcodes import Language

from spaceone.core.utils import random_string
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core.pygrpc.message_type import *

from spaceone.tester import TestCase, print_json

SCHEMA = {"properties": {
                    "sa_name": {
                        "minLength": 4,
                        "type": "string",
                        "title": "Service Account"
                    },
                    "project_id": {
                        "minLength": 4,
                        "type": "string",
                        "title": "Project ID"
                    }
                },
                "type": "object",
                "required": [
                ]
        }


PLUGIN_PARAMS = {
    'aws-ec2': {
            'name':'aws-ec2',
            'service_type':'inventory.Collector',
            'image':'pyengine/aws-ec2',
            'labels': ['Server'],
            'provider': 'aws',
            'capability': {
                'supported_schema': ["aws_access_key"]
            },
            'template': {'options': {'schema': SCHEMA}},
            "tags": {
                "icon": "https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-ec2.svg",
                "description": "AWS EC2 Compute collector",
                "spaceone:plugin_name": "aws-ec2"
                }
        },

    'aws-cloud-services': {
            'name':'aws-cloud-services',
            'service_type':'inventory.collector',
            'image':'pyengine/aws-cloud-services',
            'labels': ['DynamoDB', 'S3', 'ElastiCache', 'AutoScaling Group', 'DirectConnector', 'RDS', 'DocumentDB',
                       'EKS', 'Redshift', 'EFS', 'ECS', 'Workspace', 'API Gateway', 'Route53',
                       'SQS', 'ECR', 'CloudTrail', 'SNS', 'SecretManager', 'AmazonAthena' 'KMS', 'Kinesis'],
            'provider': 'aws',
            'capability': {
                'supported_schema': ["aws_access_key"]
            },
            'template': {'options': {'schema': SCHEMA}},
            "tags": {
                "icon": "https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-cloudservice.svg",
                "description": "AWS Cloud Services collector",
                "spaceone:plugin_name": "aws-cloud-services"
                }
        },

    'gcp-compute': {
            'name': 'gcp-compute',
            'service_type':'inventory.collector',
            'image':'pyengine/gcp-compute',
            'labels': ['Server'],
            'provider': 'google_cloud',
            'capability': {
                'supported_schema': ["google_application_credentials"]
            },
            'template': {'options': {'schema': SCHEMA}},
            'tags' : {
                "icon": "https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/gcp-compute.svg",
                "description": "Google Compute Engine collector",
                "spaceone:plugin_name": "gcp-compute"
                }
        },
    'cloud-watch': {
            'name': 'aws-cloud-watch',
            'image': 'pyengine/aws-cloudwatch',
            'service_type': 'monitoring.DataSource',
            'provider': 'aws',
            'capability': {
                'use_resource_secret': True,
                'monitoring_type': 'METRIC',
                'supported_schema': ['aws_access_key', 'aws_assume_role']
            },
            'labels': ['Monitoring', 'AWS', 'CloudWatch'],
            'tags': {
                'description': 'AWS CloudWatch Monitoring Plugin',
                'icon': 'https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-cloudwatch.svg',
                'spaceone:plugin_name': 'aws-cloud-watch'
            }
        },
    'aws-health': {
            'name':'aws-health',
            'image':'pyengine/aws-health',
            'service_type':'monitoring.DataSource',
            'provider': 'aws',
            'capability': {
                'use_resource_secret': True,
                'monitoring_type': 'LOG',
                'supported_schema': ['aws_access_key', 'aws_assume_role']
            },
            'labels': ['Monitoring', 'AWS', 'Personal_Health_Dashboard'],
            "tags": {
                "icon": "https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-phd.svg",
                "description": "AWS Personal Health Monitoring Plugin",
                "spaceone:plugin_name": "aws-health"
                }
        },
    'aws-cloud-trail': {
            'name':'aws-cloud-trail',
            'service_type':'monitoring.DataSource',
            'image':'pyengine/aws-cloudtrail',
            'provider': 'aws',
            'capability': {
                'use_resource_secret': True,
                'monitoring_type': 'LOG',
                'supported_schema': ['aws_access_key', 'aws_assume_role']
            },
            'labels': ['Monitoring', 'AWS', 'CloudTrail'],
            "tags": {
                "icon": "https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-cloudtrail.svg",
                "description": "AWS CloudTrail Monitoring Plugin",
                "spaceone:plugin_name": "aws-cloud-trail"
                }
        },
    'google-oauth2': {
            'name':'google-oauth2',
            'service_type':'identity.domain',
            'template': {
                'options':
                  [
                    {"key":"domain","name":"Top domain name", "type":"str", "is_required":False, "example":"Domain name of Company (ex. gmail.com)"},
                    {"key": "client_id", "name":"Oauth Client ID", "type":"string", "is_required":True, "example":"OAuth 2.0 Client ID"}
                  ],
            },
            'image':'pyengine/googleoauth2',
            'tags' : {
                "icon": "https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/google-icon.svg",
                "description": "Google OAuth2 Authentication",
                "spaceone:plugin_name": "google-oauth2"
                }
            }
}





class TestRepository(TestCase):

    def _create_plugin(self, params):
        """" Create Plugin based on params

        """

        params.update({'domain_id': self.domain.domain_id})
        print(params)
        plugin = self.repository.Plugin.register(params, metadata=self.meta)
        print_json(plugin)

        return plugin

    def test_create(self):
        for key, plugin_param in PLUGIN_PARAMS.items():
            self._create_plugin(plugin_param)

if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
