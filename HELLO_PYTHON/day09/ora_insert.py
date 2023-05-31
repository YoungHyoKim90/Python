import cx_Oracle as cx
        
def my_insert(e_id, e_name=None, gen=None, addr=None):
    # DB 연결하기
    conn = cx.connect("python","python","127.0.01:1521/XE") 
    cur = conn.cursor()

    ### 쿼리문 작성 후 작성 후 실행
        
    ## 1번 방식
    # sql = """insert into emp(e_id, e_name, gen, addr)
    #          values(:1,:2,:3,:4)""" 
    # cur.execute(sql,[e_id, e_name, gen, addr]) #[값]
    
    ## 2번 방식
    sql = f"""
        insert into emp
            (e_id, e_name, gen, addr)
        values
            ('{e_id}','{e_name}','{gen}','{addr}')
        """ 
    cur.execute(sql) #[값]
    conn.commit()
    
    cur.close()
    conn.close()

# main
my_insert('4', '4', '4', '4')