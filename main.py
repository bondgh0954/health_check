import boto3 as bt

client = bt.client('ec2')

my_instances = client.describe_instances()
instance_status = client.describe_instance_status()

inst_stat = instance_status['InstanceStatuses']

instances_rev = my_instances['Reservations']
for instances in instances_rev:
    my_instances = instances['Instances']
    for instance_info in my_instances:
        instance_id = instance_info['InstanceId']
        state = instance_info['State']['Name']
        for status in inst_stat:
            this_stat = status['InstanceStatus']['Status']


            print(f"EC2 instance with ID number {instance_id} is {state} and its health is {this_stat}")



