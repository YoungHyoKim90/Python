import cx_Oracle

from day09.ora_delete import sql


class DaoMem:

    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor() 
    
    def select_list(self): 
        ret = []
        sql = """
            select 
                m_id,m_nm,tel,address 
            from 
                mem
        """
        rs = self.cs.execute(sql)
        for r in rs:
            ret.append({'m_id':r[0], 'm_nm':r[1], 'tel':r[2], 'address':r[3]})
            
        return(ret)
    
    def select_one(self, m_id):
        ret = []
        sql = f"""
            select 
                m_id,m_nm,tel,address  
            from
                mem
            where 
                m_id = '{m_id}'
        """
        rs = self.cs.execute(sql)
        for r in rs:
            ret.append({'m_id':r[0], 'm_nm':r[1], 'tel':r[2], 'address':r[3]})
            
        return ret[0]
        
    def __del__(self):
        self.cs.close()
        self.conn.close()
        
    def insert (self, m_nm, tel, address):
        ret = []
        sql = f"""
            insert into mem
                (m_id,m_nm,tel,address)  
            values
                (m_seq.nextval,'{m_nm}','{tel}','{address}')
            
        """
        self.cs.execute(sql)
        self.conn.commit()
        return self.cs.rowcount
    
    def update (self, m_id, m_nm, tel, address):
        
        ret = []
        sql = f'''
            UPDATE 
                mem 
            SET 
                m_nm = '{m_nm}', tel = '{tel}', address = '{address}' 
            WHERE 
                m_id = '{m_id}'

        '''
        self.cs.execute(sql)
        self.conn.commit()
        return self.cs.rowcount
    
    def delete (self,m_id):
        ret=[]
        sql = f'''
            DELETE FROM 
                mem 
            WHERE 
                m_id = '{m_id}'
        '''
        self.cs.execute(sql)
        self.conn.commit()
        return self.cs.rowcount
    
        
if __name__ == '__main__':
    de = DaoMem()
    cnt = de.delete("2")
    print(cnt)
