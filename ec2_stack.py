from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class MyEC2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define a VPC
        vpc = ec2.Vpc(self, "MyVPC", max_azs=2)

        # Define an EC2 instance
        instance = ec2.Instance(self, "MyEC2Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc
        )

app = core.App()
MyEC2Stack(app, "MyEC2Stack")
app.synth()