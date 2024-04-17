from troposphere import Template, Parameter, Ref, Output, route53

# Create a new CloudFormation template
template = Template()

# Define a parameter for the domain name
domain_name_param = template.add_parameter(Parameter(
    "DomainName",
    Type="String",
    Description="wheretolivehki.com"
))

# Define a Route 53 record set
record_set = route53.RecordSetGroup(
    "MyRecordSet",
    HostedZoneId="",  # Specify the hosted zone ID
    RecordSets=[
        route53.RecordSet(
            Name=Ref(domain_name_param),  # Use the domain name parameter
            Type="A",
            TTL="300",
            ResourceRecords=["10.0.0.1"]  # Example IP address
        )
    ]
)

# Add the record set to the template
template.add_resource(record_set)

# Output the CloudFormation template
print(template.to_yaml())
