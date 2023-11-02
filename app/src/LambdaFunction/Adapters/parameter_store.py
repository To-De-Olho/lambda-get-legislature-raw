import boto3

client = boto3.client("ssm", "sa-east-1")

def get_parameters(params: list):
    response = client.get_parameters(Names=params)['Parameters']
    dict = {}
    for values in response:
        dict[values['Name']] = values['Value']

    return dict