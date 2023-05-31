import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

# 새로운 행을 추가할 데이터
e_id = "4"
e_name = "4"
gen = "4"
addr = "4"

# INSERT 문 실행
sql = f"""
    update emp set 
e_name = '{e_name}', gen = '{gen}', addr ='{addr}'where e_id = '{e_id}';
"""



# INSERT 문 실행
cs.execute(sql)


print("INSERT 성공!")

conn.commit()
cs.close()
conn.close()
