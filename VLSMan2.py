#Begin Program
subnets = ['255.255.255.255', '255.255.255.252']
#Initalization Complete
print("System Initalized, Welcome To VLSMan 2.1")
print("////////////////////////////////////////////////////////////")

#Main Code, will keep running until break.
while True:

    #Program needs to take input from user: HostsNeeded;
    hostsNeeded = int(input("Enter a numerical value below:\n"))

    #LOGIC ENGINE ----------------
    n=0
    while (pow(2,n) - 2) <= hostsNeeded:
        print(n)
        n = n + 1
    hostBitsNeeded = n

    print("Value was " + str(n))

    continue