class Item:
    def __init__(self,name="Oreo Biscuits",price=0,category="Food"):
        self.name = name
        self.price = price
        self.category=category
        if self.price <= 0:
            raise ValueError(f'Invalid value for price, got {self.price}')
        
    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"
        
class Query:
    li = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
    def __init__(self,field="name", operation="EQ", value="Oreo Biscuits"):
        self.field = field
        self.operation = operation
        self.value = value
        
        if self.operation not in Query.li:
            raise ValueError(f'Invalid value for operation, got {self.operation}')
        
    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"


class Store:
    def __init__(self):
        self.store_item = []
        
    def __str__(self):
        if self.store_item == []:
            return 'No items'
        return '\n'.join(map(str,self.store_item))
        
    def add_item(self,item):
        self.store_item.append(item)
        
    def count(self):
        return len(self.store_item)    
        
        
    def filter(self,query):
        store_obj = Store()
        
        for item in self.store_item:
            item_value = getattr(item,query.field)
        
            if query.operation == "EQ" and item_value == query.value:
                store_obj.add_item(item)
            elif query.operation == "IN" and item_value in query.value:
                store_obj.add_item(item)
            elif query.operation == "GT" and item_value > query.value:
                store_obj.add_item(item)
            elif query.operation == "GTE" and item_value >= query.value:
                store_obj.add_item(item)
            elif query.operation == "LT" and item_value < query.value:
                store_obj.add_item(item)
            elif query.operation == "LTE" and item_value <= query.value:
                store_obj.add_item(item)
            elif query.operation == "STARTS_WITH" and item_value.startswith(query.value):
                store_obj.add_item(item)
            elif query.operation == "ENDS_WITH" and item_value.endswith(query.value):
                store_obj.add_item(item)
            elif query.operation == "CONTAINS" and query.value in item_value:
                store_obj.add_item(item)
                
                
        return store_obj
        
       
    def exclude(self,query):
        exclude_obj = Store()
        res = self.filter(query)

        for item in self.store_item:
            if item not in res.store_item:
                exclude_obj.add_item(item)
                
        return exclude_obj
        
"""
class Store:
    def __init__(self):
        self.item_list = []
        
    def add_item(self,item=None):
        self.item_list.append(item) 
        
        
    def __str__(self):
        if self.item_list == []:
            return "No items"
        else:
            return  '\n'.join(map(str,self.item_list))
    
            
            
    def count(self):
        return len(self.item_list)
            
        
    def filter(self,query):
        store_obj = Store()
        if query.operation == 'EQ':
            
            for item in self.item_list:
                if query.value == item.name:
                    store_obj.add_item(item)
                
                elif query.value == item.price:
                    store_obj.add_item(item)
                    
                elif query.value == item.category:
                    store_obj.add_item(item)
            
        elif query.operation == 'GT':
            
            for item in self.item_list:
                if query.value < item.price:
                    store_obj.add_item(item)
            
            
        elif query.operation == 'LT':
            
            for item in self.item_list:
                if query.value > item.price:
                    store_obj.add_item(item)
            
        
        elif query.operation == 'GTE':
            
            for item in self.item_list:
                if query.value <= item.price:
                    store_obj.add_item(item)
            
        elif query.operation == 'LTE':
            
            for item in self.item_list:
                if query.value >= item.price:
                    store_obj.add_item(item)
           
        elif query.operation == 'STARTS_WITH':
            
            for item in self.item_list:
                if  item.name.startswith(query.value) == True:
                    store_obj.add_item(item)
                elif item.category.startswith(query.value) == True:
                    store_obj.add_item(item)
            
        elif query.operation == 'ENDS_WITH':
            
            for item in self.item_list:
                if  item.name.endswith(query.value) == True:
                    store_obj.add_item(item)
                elif item.category.endswith(query.value) == True:
                    store_obj.add_item(item)
            
            
        elif query.operation == 'IN':
            
            for item in self.item_list:
                if item.name in query.value:
                    store_obj.add_item(item)
                elif item.category in query.value:
                    store_obj.add_item(item)
                elif item.price in query.value:
                    store_obj.add_item(item)
                    
                
        elif query.operation == 'CONTAINS':
            
            for item in self.item_list:
                if (query.field == "name" and item.name.__contains__(query.value)) or (query.field == "category" and item.category.__contains__(query.value)):
                    store_obj.add_item(item)
                    
        return store_obj     
            
    def exclude(self,query):
        store_obj = Store()
        if query.operation == 'EQ':
            
            for item in self.item_list:
                if query.value != item.name and query.value != item.price and query.value != item.category:
                    store_obj.add_item(item)
                    
            
        elif query.operation == 'GT':
            
            for item in self.item_list:
                if query.value >= item.price:
                    store_obj.add_item(item)
                    
            
        elif query.operation == 'LT':
            
            for item in self.item_list:
                if query.value <= item.price:
                    store_obj.add_item(item)
                    
        
        elif query.operation == 'GTE':
            
            for item in self.item_list:
                if query.value > item.price:
                    store_obj.add_item(item)
                    
        elif query.operation == 'LTE':
            
            for item in self.item_list:
                if query.value < item.price:
                     store_obj.add_item(item)
                    
        elif query.operation == 'STARTS_WITH':
            for item in self.item_list:
                if not(item.name.startswith(query.value)or item.category.startswith(query.value)):
                    store_obj.add_item(item)
                
        elif query.operation == 'ENDS_WITH':
            for item in self.item_list:
                if not(item.name.endswith(query.value) or item.category.endswith(query.value)):
                    store_obj.add_item(item)
		
            
            
            
        elif query.operation == "IN":
            for item in self.item_list:
                if (item.name not in query.value) and (item.category not in query.value) and (item.price not in query.value):
                    store_obj.add_item(item)
		
        elif query.operation == "CONTAINS":
            if query.field == "name":
                for item in self.item_list:
                    if not(item.name.__contains__(query.value)):
                        store_obj.add_item(item)
            else:
                for item in self.item_list:
                    if not(item.category.__contains__(query.value)):
                        store_obj.add_item(item)
                
        return store_obj
                
                
class Item:
    def __init__(self,name=None,price=0,category=None):
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
          
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self):
        return f'{self.name}@{self.price}-{self.category}'
        
class Query:
    operations = ["IN","EQ","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
    def __init__(self,field=None,operation=None,value=None):
        self.field = field
        self.operation = operation
        self.value = value
        
        if self.operation not in self.operations:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
            
        
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'        
        
"""
            