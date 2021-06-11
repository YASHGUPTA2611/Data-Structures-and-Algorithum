# First we create nodes then linked lists, add nodes to linked lists, print linked lists.

# STEPS -> 1. made an object to node class. 

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newnode):
	  
		if self.head is None:
			self.head = newnode
		else:
			lastnode = self.head
			while True:
				if lastnode.next is None:
					break
				lastnode = lastnode.next
			lastnode = newnode
	
	def printlist(self):

		if self.head is None:
			print("The list is empty")
			return
		currentnode = self.head
		while True:

			if currentnode.next is None:
				break
			print(currentnode.data)
			currentnode = currentnode.next


first_node = Node("john")
linkedList = LinkedList()
linkedList.insert(first_node)
second_node = Node("Ben")
linkedList.insert(second_node)
third_node = Node("Matthew")
linkedList.insert(third_node)
linkedList.printlist()



