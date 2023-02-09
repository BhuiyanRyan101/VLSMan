import sys
import time
print("Welcome To VLSMan 1.0")
print("/////////////////////")

hosts = int(input("Please enter number of hosts needed: \n"))
n=0
while (pow(2,n)-2) < hosts:
  n += 1

subnets = ["255.255.255.255", "255.255.255.254", "255.255.255.252"]

if(n==1):
  print("Subnetting Error")
  sys.exit()

print("Reccomended Subnet is: " + hosts[n])

time.sleep(10)
input("Press any key to quit.")
sys.exit()