from troposphere import Template, Ref, Parameter, ec2

# Create a template
template = Template()

# Define parameters
key_name_param = template.add_parameter(Parameter(
    "KeyName",
    Type="String",
    Description="Name of an existing EC2 KeyPair to enable SSH access to the instance",
    Default="main",
))

# Define EC2 instance
ec2_instance = ec2.Instance(
    "WhereToLiveHost",
    ImageId="ami-0d3a2960fcac852bc",  # Amazon Linux 2023 AMI ID
    InstanceType="t3.nano",
    KeyName=Ref(key_name_param),
)

# Add the EC2 instance to the template
template.add_resource(ec2_instance)

# Define security group (Amazon Linux 2023)
linux_sg = ec2.SecurityGroup(
    "AmazonLinuxSecurityGroup",
    GroupDescription="Allow SSH access from my Vantaa IP",
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="176.72.100.93/32",  # Your IP address
        ),
        # Add HTTP ingress rule to Amazon Linux security group
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=80,
            ToPort=80,
            CidrIp="0.0.0.0/0",  # My IP
        ),
    ],
)

# Add the security group to the template
template.add_resource(linux_sg)

# Attach the security group to the EC2 instance
ec2_instance.SecurityGroups = [Ref(linux_sg)]

# Print the CloudFormation template
print(template.to_yaml())