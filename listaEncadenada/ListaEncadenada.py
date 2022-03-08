class ListaEncadenada:
    def __init__(self):
        self.head=None
        
    def insertaNodo(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            index = self.head
            while index.next != None:
                index=index.next
            index.next=new_node
        
	## check whether the head is empty or not
        # if self.head:
		# ## getting the last node
        #     last_node = self.head
        #     while last_node != None:
        #         last_node = last_node.next
		# ## assigning the new node to the next pointer of last node
        #     last_node.next = new_node
        # else:
		# ## head is empty
		# ## assigning the node to head
        #     self.head = new_node
        
    def imprimeLista(self):
        index=self.head
        while index!=None:
            print(index.nombre)
            index=index.next
            
    def buscaNodo(self,id):
        index=self.head
        while index.getId() != id :
            index = index.next
        return index
    
    def eliminaNodo(self,id):
        if self.head==None:
            return 'lista encadenada vacía'
        else:
            index = self.head
            if index.getId()==id:
                index = index.next
                index.next = None
                return 'deleted'
            else:
                before_index=index
                index=index.next
                while index.getId()!=id:
                    index=index.next
                    before_index=before_index.next
                