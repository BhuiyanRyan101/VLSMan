import time
print("Welcome To VLSMan 1.1")
print("////////////////////////////////////////////////////////////")

while True:

  hosts = int(input("\nPlease enter number of hosts needed:\n"))
  n=0
  while (pow(2,n)-2) < hosts:
    n += 1

  subnets = ["255.255.255.255", "255.255.255.254", "255.255.255.252","255.255.255.248","255.255.255.240","255.255.255.224","255.255.255.192","255.255.255.128","255.255.255.0","255.255.254.0","255.255.252.0","255.255.248.0","255.255.240.0","255.255.224.0","255.255.192.0","255.255.128.0","255.255.0.0"]

  if(n==1 or n>len(subnets)-1):
    print("\nSubnetting Error")
    input("\nPress any key to try again")
    continue

  print("\nReccomended Subnet is: " + subnets[n])
  input("\nPress any key to try again.")
  continue