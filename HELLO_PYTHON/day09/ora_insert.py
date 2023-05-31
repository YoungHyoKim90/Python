import cx_Oracle


conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

df_list = df.to_records(index=False)

rs.executemany("INSERT INTO emp (e_id,e_name,gen,addr) VALUES ('3','3','3','3')",
            df_list, batcherrors = True)

rs = cs.execute(sql)

for r in rs:
    print(r)
    
con.commit()
    
cs.close()
conn.close()

