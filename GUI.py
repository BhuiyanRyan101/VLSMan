# Program to make a simple 
# login screen 

from VLSMan4 import vlsman
import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("500x180")
root.title("VLSMan")

# declaring string variable
# for storing hosts and networkAddress
hosts_var=tk.IntVar()
netAdd_var=tk.StringVar()

#Make the results in a readable format
def formatResults(resultsMatrix):
	return("Results:\n" + "Network Address: " + resultsMatrix[0] + "\nBroadcast Address: " + resultsMatrix[1] + "\nAssignable Range: " + resultsMatrix[2] + " - " + resultsMatrix[3] + "\nSubnet Mask: " + resultsMatrix[4])

#On button press
def submit():
	
	hostsNeeded = int(hosts_var.get())
	networkAddress = str(netAdd_var.get())
	resultsMatrix = vlsman(hostsNeeded,networkAddress)
	results_label.config(text = formatResults(resultsMatrix))


# creating a label for the number of hosts needed
hosts_label = tk.Label(root, text = 'Hosts Needed', font=('calibre',10, 'bold'), anchor="w", justify="left")

# creating a entry for the number of hosts needed
hosts_entry = tk.Entry(root,textvariable = hosts_var, font=('calibre',10,'normal'))

# creating a label for the Network Address
netAdd_label = tk.Label(root, text = 'Network Address', font = ('calibre',10,'bold'), anchor="w", justify="left")

# creating a entry for the Network Address
netAdd_entry=tk.Entry(root, text = 'x.x.x.x', textvariable = netAdd_var, font = ('calibre',10,'normal'))

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Calculate', command = submit)

# creating a label for the number of hosts needed
results_label = tk.Label(root, text = 'Results:\nNetwork Address:\nBroadcast Address:\nAssignable Range:\nSubnet Mask::', font=('calibre',10, 'bold'), anchor="w", justify="left")

# placing the label and entry in
# the required position using grid
# method
hosts_label.grid(row=0,column=0)
hosts_entry.grid(row=0,column=1)
netAdd_label.grid(row=1,column=0)
netAdd_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
results_label.grid(row=3,column=0)

# performing an infinite loop 
# for the window to display
root.mainloop()


