from troposphere import Template, route53

# Create a new CloudFormation template
template = Template()

# Define the hosted zone
hosted_zone = route53.HostedZone(
    "MyHostedZone",
    Name="wheretolivehki.com",  # Replace with your domain name
    HostedZoneConfig=route53.HostedZoneConfiguration(
        Comment="My first hosted zone on Route 53"
    )
)

# Add the hosted zone to the template
template.add_resource(hosted_zone)

# Print the CloudFormation template
print(template.to_yaml())
