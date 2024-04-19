from troposphere import Template, route53

# Create a new CloudFormation template
template = Template()

# Define the hosted zone
hosted_zone = route53.HostedZone(
    "Portfolio",
    Name="matiaskuismanen.ddns.net",  # Replace with your domain name
    HostedZoneConfig=route53.HostedZoneConfiguration(
        Comment="The hosted zone for the DNS name specified here."
    )
)

# Add the hosted zone to the template
template.add_resource(hosted_zone)

# Create an A record for the root of the subdomain
a_record = route53.RecordSetType(
    "RootRecord",
    HostedZoneName="matiaskuismanen.ddns.net.",
    Name="matiaskuismanen.ddns.net.",
    Type="A",
    TTL="300",
    ResourceRecords=["18.192.182.207"]
)

# Add the A record to the template
template.add_resource(a_record)

# Print the CloudFormation template
print(template.to_yaml())
