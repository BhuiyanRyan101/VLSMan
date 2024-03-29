#VLSMan 4.1
#Begin Program and Define Variables
subnets = ["255.255.255.255", "255.255.255.254", "255.255.255.252","255.255.255.248","255.255.255.240","255.255.255.224","255.255.255.192","255.255.255.128","255.255.255.0","255.255.254.0","255.255.252.0","255.255.248.0","255.255.240.0","255.255.224.0","255.255.192.0","255.255.128.0","255.255.0.0","255.254.0.0","255.252.0.0","255.248.0.0","255.240.0.0","255.224.0.0","255.192.0.0","255.128.0.0","255.0.0.0"]
#Main VLSMan Function
def vlsman(hostsNeeded, networkAddress):

    #ErrorDetection
    if int(networkAddress[-1]) % 2 != 0:
        print("\nThe specified network address is not a network address! Please try again!\n")

    #Calculate number of host bits needed.
    bitsNeeded = 0
    while True:
        usableHosts = pow(2,bitsNeeded) - 2
        if usableHosts >= hostsNeeded or hostsNeeded == 0:
            break
        bitsNeeded += 1

    #Get subnet mask
    subnetMask = subnets[bitsNeeded]

    #Make the subnet mask an index for calculation purposes.
    subnetMaskMatrix = ["","","",""]
    workingSubnetOctect = 0
    index = 0
    while True:
        character = subnetMask[index]
        if character == '.':
            workingSubnetOctect += 1
            index += 1
            continue
        subnetMaskMatrix[workingSubnetOctect] += character
        if index == len(subnetMask)-1:
            break
        index += 1

    #Make the networkAddress an index for calculation purposes.
    networkAddressMatrix = ["","","",""]
    workingNetAddOctect = 0
    j = 0
    while True:
        character = networkAddress[j]
        if character == '.':
            workingNetAddOctect += 1
            j += 1
            continue
        networkAddressMatrix[workingNetAddOctect] += character
        if j == len(networkAddress)-1:
            break
        j += 1

    #Calculate the wildcard mask
    wildcardMaskMatrix = ["","","",""]
    wildcardMaskMatrix[0] = str(255-int(subnetMaskMatrix[0]))
    wildcardMaskMatrix[1] = str(255-int(subnetMaskMatrix[1]))
    wildcardMaskMatrix[2] = str(255-int(subnetMaskMatrix[2]))
    wildcardMaskMatrix[3] = str(255-int(subnetMaskMatrix[3]))

    #Calculate the broadcast address
    broadcastAddress = str(int(networkAddressMatrix[0]) + int(wildcardMaskMatrix[0])) + '.'
    broadcastAddress += str(int(networkAddressMatrix[1]) + int(wildcardMaskMatrix[1])) + '.'
    broadcastAddress += str(int(networkAddressMatrix[2]) + int(wildcardMaskMatrix[2])) + '.'
    broadcastAddress += str(int(networkAddressMatrix[3]) + int(wildcardMaskMatrix[3]))

    #Calculate the assignable address range
    firstAssignableAddress = networkAddressMatrix[0] + "." + networkAddressMatrix[1] + "." + networkAddressMatrix[2] + "." + str(int(networkAddressMatrix[3]) + 1)
    lastAssignableAddress = (str(int(networkAddressMatrix[0]) + int(wildcardMaskMatrix[0]))) + "." + (str(int(networkAddressMatrix[1]) + int(wildcardMaskMatrix[1]))) + "." + (str(int(networkAddressMatrix[2]) + int(wildcardMaskMatrix[2]))) + "." + (str(int(networkAddressMatrix[3]) + int(wildcardMaskMatrix[3]) - 1))

    #Debug Printer.
    #print("Broadcast Address: " + broadcastAddress)
    #print("Wildcard Matrixes: " + str(wildcardMaskMatrix))
    #print("Network Matrixes: " + str(networkAddressMatrix))
    #print("Subnet Matrixes: " + str(subnetMaskMatrix))
    #print("Use subnet: " + subnetMask)
    #print(int(networkAddress[-1]) % 2)

    #Debug Printer
    print("\nResults:")
    print("Network Address is: " + networkAddress)
    print("Broadcast Address is: " + broadcastAddress)
    print("Assignable Range is: " + firstAssignableAddress + " - " + lastAssignableAddress)
    print("Subnet Mask is: " + subnetMask)

    #Return to caller via matrix [networkAddress, broadcastAddress, firstAssignableAddress, lastAssignableAddress, subnetMask]
    return([networkAddress,broadcastAddress,firstAssignableAddress,lastAssignableAddress,subnetMask])

#Made by Ryan Bhuiyan