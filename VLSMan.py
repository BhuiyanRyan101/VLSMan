#Start the program
import time
print("Welcome To VLSMan 1.1")
print("////////////////////////////////////////////////////////////")

#Main Code, Keeps code looping
while True:

  hosts = int(input("\nPlease enter number of hosts needed:\n"))
  n=0
  while (pow(2,n)-2) < hosts:
    n += 1

  #Array lists of subnets /32 to /16
  subnets = ["255.255.255.255", "255.255.255.254", "255.255.255.252","255.255.255.248","255.255.255.240","255.255.255.224","255.255.255.192","255.255.255.128","255.255.255.0","255.255.254.0","255.255.252.0","255.255.248.0","255.255.240.0","255.255.224.0","255.255.192.0","255.255.128.0","255.255.0.0"]

  #Ends program early if cannot subnet or not supported yet
  if(n==1 or n>len(subnets)-1):
    print("\nSubnetting Error")
    input("\nPress any key to try again")
    continue

  print("\nReccomended Subnet is: " + subnets[n])
  input("\nPress any key to try again.")
  continue
  
  #VLSMan is made by Ryan Bhuiyan
