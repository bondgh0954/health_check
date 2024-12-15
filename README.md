# health_check Demo Project

# Technologies used
Python  :  boto3 library
AWS


# Project Description
1. Create EC2 instances with Terraform
2. Write a Python script that fetches statuses of EC2 instances and prints to the console
3. Extend the python script to continuously check the status of EC2 instances in a specific interval



# Project Introduction and Motivation

Assuming 100s of EC2 servers have been created using terraform in your cloud platform account with autoscaling configured.
This means there is always the creation of new instances and deletion of instances as the need arises automatically.
EC2 instances need some time to initialize there is the need to know which instances are in which state to get the overview of which instances are running, ready state, or which ones are initializing.
There python boto library is utilized in creating a script that checks the health of the EC2 instances.

# Steps
create 3 EC2 instances on aws 

import the boto3 library in python and call the client function on the library

       import boto3 as bt
       client = bt.client('ec2')

call the describe_instances function on the client and without passing in parameters list all available instances

       my_instances = client.describe_instances()


Loop through the Reservations which containers list of instances and by using the keys of the dictionary you obtain the values of InstaceID and State and status check which are printed in the console

NB: Details of code can be found in main.py file in the repo:


<img src='./Screenshot from 2024-12-15 11-01-57.png' height="80%" width="80%" alt="Disk Sanitization Steps">



      


       
       



