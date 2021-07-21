class DLLNode:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.previous = None 
    
    def __repr__(self):
        return "DLLNode Object: {}".format(self.data)
    
    def get_data(self):
        """ Returns the self.data attribute of the Node object """
        return self.data 
    
    def set_data(self, new_data):
        """ Replaces the self.data attribute of the Node Object with the new_data """
        self.data = new_data 
    
    def get_next(self):
        """ Returns the self.next attribute of the Node Object """
        return self.next 
    
    def get_previous(self):
        """ Returns the self.previous attribute of the Node Object in the DLL"""
        return self.previous
    
    def set_next(self, new_next):
        """ Replace the self.next attribute of the Node Object in DLL with new_next """
        self.next = new_next
    
    def set_previous(self,new_previous):
        """ Replaces the self.previous attribute of the Node Object with the new_previous"""
        self.previous = new_previous
    
