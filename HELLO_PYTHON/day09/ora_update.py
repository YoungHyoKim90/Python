import cx_Oracle

# Oracle 데이터베이스 연결 정보
conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

# 업데이트할 데이터
e_id = "3"
e_name = "6"
gen = "6"
addr = "6"

# UPDATE 문 실행
sql = f"UPDATE emp SET e_name = '{e_name}', gen = '{gen}', addr = '{addr}' WHERE e_id = '{e_id}'"

# UPDATE 문 실행
cs.execute(sql)

print("UPDATE 성공!")

# 변경사항 커밋
conn.commit()

# 리소스 정리
cs.close()
conn.close()
