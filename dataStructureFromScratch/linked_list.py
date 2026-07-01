class Node:
	def __init__ (self , data):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
	def insert_at_beginning(self , data):
		new_node=Node(data)
		new_node.next=self.head
		self.head=new_node
	def insert_at_end(self , data):
                new_node=Node(data)
               	current=self.head
               	if self.head is None:
                       	self.head=new_node
                       	return 
                while(current.next!=None):
                        current=current.next
               	current.next=new_node
	def insert_at_position(self , data , position):
		new_node=Node(data)
		counter=0
		current=self.head
		if self.head is None:
			self.head=new_node
			return
		if position==0:
			self.insert_at_beginning(data)
		while(current is not None):
			if counter ==position-1:
				new_node.next=current.next
				current.next=new_node
				return
			current=current.next
			counter+=1
	def delete_at_beginning(self):
                current=self.head
                if self.head is None:
                        return
                self.head=self.head.next
               	current.next=None
	def delete_at_end(self):
               	if self.head is None:
                       	return
               	current=self.head
               	if self.head.next is None:
                       	self.head=None 
                       	return
                while current.next.next!=None :
                               	current=current.next
                tofree=current.next
                current.next=None
                tofree.next=None
	def delete_at_position(self,position):
                current=self.head
                if self.head is None :
                        print("Linked list is empty.")
                        return
                counter=0
                if position==0:
                        self.delete_at_beginning()
                        return 
                while current is not None:
                                if counter==position-1:
                                        if current.next is None:
                                                        print("Position out of range")
                                                        return
                                        tofree=current.next
                                        current.next=current.next.next
                                        tofree.next=None
                                        return
                                current=current.next
                                counter+=1
	def display(self):
		current=self.head 
		if self.head is None:
			print("Empty list.")
			return
		while(current is not None):
			print(current.data)
			current=current.next
	def search(self,data):
		counter=0
		current=self.head
		if  self.head is None:
			print("Empty list.")
			return 
		while(current is not None):
			if current.data==data:
				print("Element is present. at" , counter , "position")
				return
			current=current.next
			counter+=1
		print("Element is absent")
ll=LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(6)
ll.insert_at_end(4)
#ll.delete_at_end()
#ll.delete_at_beginning()
#ll.insert_at_position(3,2)
ll.delete_at_position(3)
ll.display()



