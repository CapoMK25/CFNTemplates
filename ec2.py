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
    "PortfolioHost",
    ImageId="ami-0afcbcee3dfbce929",  # CentOS AMI ID
    InstanceType="t3.nano",
    KeyName=Ref(key_name_param),
)

# Add the EC2 instance to the template
template.add_resource(ec2_instance)

# Define security group
ssh_sg = ec2.SecurityGroup(
    "SSHSecurityGroup",
    GroupDescription="Allow SSH access from my Turkey IP",
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="185.117.123.142/32",  # Your IP address
        ),
    ],
)

# Add the security group to the template
template.add_resource(ssh_sg)

# Attach the security group to the EC2 instance
ec2_instance.SecurityGroups = [Ref(ssh_sg)]

# Print the CloudFormation template
print(template.to_yaml())