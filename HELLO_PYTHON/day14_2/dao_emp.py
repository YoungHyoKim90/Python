import cx_Oracle

class DaoEmp:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()   
    
    def select_list(self):
        ret = []
        sql = '''
            select 
                e_id,e_name,gen,addr 
            from 
                emp
        '''
        rs = self.cs.execute(sql)
        for r in rs:
            ret.append({'e_id':r[0],'e_name':r[1],'gen':r[2],'addr':r[3]})
            
        return ret
    
    def select_one(self,e_id):
        ret = []
        sql = f'''
            select 
                e_id,e_name,gen,addr 
            from 
                emp
            where
                e_id = '{e_id}'
        '''
        rs = self.cs.execute(sql)
        print(rs)
        for r in rs:
            ret.append({'e_id':r[0],'e_name':r[1],'gen':r[2],'addr':r[3]})
            
        return ret[0]
    
    def insert(self,e_id,e_name,gen,addr):
        ret = []
        sql = f'''
            insert into emp 
                (e_id,e_name,gen,addr) 
            values 
                ('{e_id}','{e_name}','{gen}','{addr}')
        '''
        self.cs.execute(sql)
        self.conn.commit()   
        return self.cs.rowcount
    
    def update(self,e_id,e_name,gen,addr):
        ret = []
        sql = f'''
            update emp
            set 
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            where
                e_id = '{e_id}'
        '''
        self.cs.execute(sql)
        self.conn.commit()   
        return self.cs.rowcount
        
    def delete(self,e_id):
        ret = []
        sql = f'''
            delete from emp
            where
                e_id = '{e_id}'
        '''
        self.cs.execute(sql)
        self.conn.commit()   
        return self.cs.rowcount
    
    def __del__(self):
        self.cs.close()    
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.delete("4")
    print(cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    