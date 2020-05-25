class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score 
        self.student_id = None
    
    @staticmethod
    def get(**kwargs):
        for key, value in kwargs.items():
            if key in ['student_id','age', 'score']:
                q = 'SELECT * FROM Student WHERE {} = {}'.format(key,value)
            elif key  == 'name':
                q = 'SELECT * FROM student where {} = \'{}\' '.format(key,value);
            else:
                raise InvalidField
        query = read_data(q)    
        if len(query) == 0:
            raise DoesNotExist
        elif len(query)>1:
            raise MultipleObjectsReturned
        else:
            s = Student(query[0][1], query[0][2],query[0][3])
            s.student_id = query[0][0]
            return s
    
    def delete(self):
        q = 'DELETE FROM Student WHERE student_id = {}'.format(self.student_id);
        write_data(q)   
        
    
    def save(self):
        import sqlite3
        conn = sqlite3.connect("selected_students.sqlite3")
        crsr = conn.cursor()
        crsr.execute("PRAGMA foreign_keys= on;")
        if self.student_id == None:
            q = 'INSERT INTO Student(student_id,name,age,score) VALUES(Null,\'{}\', {},{})'.format(self.name,self.age,self.score);
            crsr.execute(q) 
            self.student_id = crsr.lastrowid
            
        elif self.name != None:
            q = 'INSERT or REPLACE INTO Student(student_id,name,age,score) VALUES({},\'{}\', {},{})'.format(self.student_id,self.name,self.age,self.score);
            crsr.execute(q) 
            
        conn.commit()
        conn.close()  
        
        
    @staticmethod
    def filter(**kwargs):
        li = []
        for key, value in kwargs.items():
            keys = key
            values = value
            
        field = keys.split('__')
        if field[0] not in ('student_id','name','age','score'):
            raise InvalidField
            
        if keys in  ('student_id','name','age','score'):
            if  key in ['student_id','age', 'score']:
                q = 'SELECT * FROM Student WHERE {} = {}'.format(key,value)
                query = read_data(q) 
        
            else:
                q = 'SELECT * FROM Student WHERE {} = \'{}\' '.format(key,value)
                query = read_data(q) 
        
            
        
        else:
            if field[1] == 'lt':
                q = 'SELECT * FROM Student WHERE {} < {}'.format(field[0],value)
                query = read_data(q) 
        
            
            if field[1] == 'gt':
                q = 'SELECT * FROM Student WHERE {} > {}'.format(field[0],value)
                query = read_data(q) 
        
                    
            if field[1] == 'lte':
                q = 'SELECT * FROM Student WHERE {} <= {}'.format(field[0],value)
                query = read_data(q) 
        
                    
            if field[1] == 'gte':
                q = 'SELECT * FROM Student WHERE {} >= {}'.format(field[0],value)
                query = read_data(q) 
        
                    
            if field[1] == 'neq':
                if  field[0] in ['student_id','age', 'score']:
                    q = 'SELECT * FROM Student WHERE {} != {}'.format(field[0],value)
                    query = read_data(q) 
        
                else:
                    q = 'SELECT * FROM Student WHERE {} != \'{}\' '.format(field[0],value)
                    query = read_data(q) 
        
               
            if field[1] == 'in':
                q = 'SELECT * FROM Student WHERE {} in {}'.format(field[0],tuple(value))
                query = read_data(q) 
        
                    
            if field[1] == 'contains':
                q = 'SELECT * FROM Student WHERE {} LIKE "%{}%" '.format(field[0],value)
                query = read_data(q) 
        
        
        if len(query) == 0:
            return []
            
        else:
            for i in range(len(query)):
                ans = Student(query[i][1],query[i][2],query[i][3])
                ans.student_id = query[i][0]
                li.append(ans)
            return li   

                
            
    


def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;")  
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
    
   

    
    






"""
s = Student(query[0][1], query[0][2],query[0][3])
s.student_id = query[0][0]
for key, value in kwargs.items():
            a,b = key.split('__')
            if b == 'lt':
                if a in ['student_id','age', 'score']:
                    q = 'SELECT * FROM Student WHERE {} < {}'.format(a,value)
            
            elif b == 'gt':
                if a in ['student_id','age', 'score']:
                    q = 'SELECT * FROM Student WHERE {} > {}'.format(a,value)
                    
            elif b == 'lte':
                if a in ['student_id','age', 'score']:
                    q = 'SELECT * FROM Student WHERE {} <= {}'.format(a,value)
                    
            elif b == 'gte':
                if a in ['student_id','age', 'score']:
                    q = 'SELECT * FROM Student WHERE {} >= {}'.format(a,value)
                    
            elif b == 'neq':
                if a in ['student_id','age','score']:
                    q = 'SELECT * FROM Student WHERE {} != {}'.format(a,value)
            
            else:
                raise InvalidField
        query = read_data(q) 
        #print(query)
        return query
        
        
    else:
    if key in ['student_id','age', 'score']:
    q = 'SELECT * FROM Student WHERE {} = {}'.format(key,value)
    uery = read_data(q) 
        
            
                elif key  == 'name':
                    q = 'SELECT * FROM Student WHERE {} = \'{}\' '.format(key,value)
                    query = read_data(q) 
        
                
                else:
                    raise InvalidField
                
"""                   
