from troposphere import Template, iam

template = Template()

# Create a new access key for the IAM user
iam_access_key = template.add_resource(iam.AccessKey(
    "MatiasAccessKey",
    UserName="Matias",  # Associate the access key with the IAM user
))

print(template.to_yaml())
