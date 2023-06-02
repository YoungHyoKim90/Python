import cx_Oracle

# Oracle 데이터베이스 연결 정보
conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

# 삭제할 데이터
e_id = "3"

# DELETE 문 실행
sql = f"DELETE FROM emp WHERE e_id = '{e_id}'"

# DELETE 문 실행
cs.execute(sql)

# 변경사항 커밋
conn.commit()

# 리소스 정리
cs.close()
conn.close()
