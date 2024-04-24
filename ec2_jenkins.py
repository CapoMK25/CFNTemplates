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
    "JenkinsHost",
    ImageId="ami-03484a09b43a06725",  # AL2023 AMI ID
    InstanceType="t3.nano",
    KeyName=Ref(key_name_param),
)

# Add the EC2 instance to the template
template.add_resource(ec2_instance)

# Define security group (CentOS)
al2023_sg = ec2.SecurityGroup(
    "AL2023SecurityGroup",
    GroupDescription="Allow SSH access from my Turkey IP",
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="185.117.123.142/32",  # Your IP address
        ),
        # Add HTTP ingress rule to AL2023 security group
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=80,
            ToPort=80,
            CidrIp="185.117.123.142/32",  # my Turkey IP
        ),
    ],
)

# Add the security group to the template
template.add_resource(al2023_sg)

# Attach the security group to the EC2 instance
ec2_instance.SecurityGroups = [Ref(al2023_sg)]

# Print the CloudFormation template
print(template.to_yaml())