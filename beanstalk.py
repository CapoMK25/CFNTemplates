from troposphere import Template, elasticbeanstalk as eb

template = Template()

eb_application = template.add_resource(eb.Application(
    "MyApplication",
    Description="My Elastic Beanstalk Application"
))

eb_environment = template.add_resource(eb.Environment(
    "MyEnvironment",
    ApplicationName="MyApplication",  # Directly provide the application name
    Description="My Elastic Beanstalk Environment",
    SolutionStackName="64bit Amazon Linux 2023 v4.0.10 running Python 3.11",
    OptionSettings=[
        eb.OptionSetting(
            Namespace="aws:autoscaling:launchconfiguration",
            OptionName="InstanceType",
            Value="t2.nano"
        )
    ]
))

print(template.to_yaml())
