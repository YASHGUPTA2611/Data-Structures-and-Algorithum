# Create a Node class which has 2 attributes data and nextnode

class LinkedListnode:
	def __init__(self,data,nextnode=None):

		self.data=data
		self.nextnode=nextnode



# we have to connect our nodes in this manner = "3" -> "7" -> "10"

# Taking an example we are assigning the nodes value. 
node1 = LinkedListnode("3")
node2 = LinkedListnode("7")
node3 = LinkedListnode("10")

# Conneccting nodes with each other.
node1.nextnode = node2  # "3" -> "7"
node2.nextnode = node3  # "7" -> "10"

#Initializing Current node to node1
currentnode = node1
# Using while loop to print the values of node until the loop becomes false.
while True:
	if currentnode is None:
		break
	print(currentnode.data)
	currentnode = currentnode.nextnode





