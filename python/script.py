import datetime

servers = ["aws-server","azure-server"]

for s in servers :
 if "aws" in s :
  print(f"[{datetime.datetime.now()}]Aws server :{s}")
 elif "azure" in s : 
  print(f"[{datetime.datetime.now()}]Azure server :{s}")
else:  
  print(f"[{datetime.datetime.now()}]Other server :{s}")