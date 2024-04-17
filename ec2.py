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
    "MyEC2Instance",
    ImageId="ami-0f7204385566b32d0",  # Amazon Linux 2 AMI ID
    InstanceType="t3.nano",
    KeyName=Ref(key_name_param),
)

# Add the EC2 instance to the template
template.add_resource(ec2_instance)

# Print the CloudFormation template
print(template.to_yaml())