#!/usr/bin/env python
from aws_cdk import (
    aws_elasticbeanstalk as elasticbeanstalk,
    aws_ec2 as ec2,
    core,
)


class ElasticBeanstalkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC for the Elastic Beanstalk environment
        vpc = ec2.Vpc(
            self, "MyVpc",
            max_azs=2
        )

        # Create an Elastic Beanstalk application
        application = elasticbeanstalk.CfnApplication(
            self, "MyApplication",
            application_name="MyApplication"
        )

        # Create an Elastic Beanstalk environment
        environment = elasticbeanstalk.CfnEnvironment(
            self, "MyEnvironment",
            application_name=application.application_name,
            solution_stack_name="64bit Amazon Linux 2 v5.4.5 running Python 3.8",
            cname_prefix="my-env",
            tier="WebServer",
            option_settings=[
                {
                    "namespace": "aws:autoscaling:asg",
                    "option_name": "MinSize",
                    "value": "2",
                },
                {
                    "namespace": "aws:autoscaling:asg",
                    "option_name": "MaxSize",
                    "value": "6",
                },
            ],
            vpc_id=vpc.vpc_id,
            instances_role=f"ElasticBeanstalkEC2Role-{core.Aws.ACCOUNT_ID}",
        )


app = core.App()
ElasticBeanstalkStack(app, "ElasticBeanstalkStack")
app.synth()