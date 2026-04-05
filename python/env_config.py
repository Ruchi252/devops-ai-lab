env = "dev"

if env == "dev":
  instance_type = "t3.micro"
else:
   instance_type = "t2.small" 

print(f"instance_type: {instance_type}")   