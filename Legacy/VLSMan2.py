#Begin Program and Define Variables
subnets = ["255.255.255.255", "255.255.255.254", "255.255.255.252","255.255.255.248","255.255.255.240","255.255.255.224","255.255.255.192","255.255.255.128","255.255.255.0","255.255.254.0","255.255.252.0","255.255.248.0","255.255.240.0","255.255.224.0","255.255.192.0","255.255.128.0","255.255.0.0"]
#Initalization Complete
print("System Initalized, Welcome To VLSMan 2.1")
print("////////////////////////////////////////////////////////////")

#Main Code, will keep running until break.
while True:

    #Program needs to take input from user: HostsNeeded;
    hostsNeeded = int(input("\nEnter the amount of hosts needed: "))

    #Calculate number of host bits needed
    bitsNeeded = 0
    while True:
        usableHosts = pow(2,bitsNeeded) - 2
        if usableHosts >= hostsNeeded or hostsNeeded == 0:
            break
        bitsNeeded += 1
    #print(str(bitsNeeded) + " Bits need to be stolen") #debugging

    #Determine subnet to use
    print("Use subnet: " + subnets[bitsNeeded])

    continue #Keep looping program.

#Made by Ryan Bhuiyan