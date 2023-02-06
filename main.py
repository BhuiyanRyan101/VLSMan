print("Welcome To VLSMan 1.0")
print("/////////////////////")

hosts = int(input("Please enter number of hosts needed: \n"))
n=0
while (pow(2,n)-2) <= hosts:
  n += 1
  print(n)

if(n==1):
  print("Subnetting Error")

if(n==2):
  print("Reccomended Subnet: 255.255.255.252")

if(n==3):
  print("Reccomended Subnet: 255.255.255.248")

if(n==4):
  print("Reccomended Subnet: 255.255.255.240")

if(n==5):
  print("Reccomended Subnet: 255.255.255.224")