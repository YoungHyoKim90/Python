from flask import Flask,request, render_template
import cx_Oracle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello Flask!</h1>'

@app.route('/param',methods=['GET'])
def param():
    a = request.args.get('menu')
    return 'param' + a

@app.route('/post',methods=['GET','POST'])
def post():
    a = request.form.get('menu')
    return 'POST' + a

@app.route('/forw')
def forw():
    a="홍길동"
    b=["전우치","이순신","유관순"]
    c=[
        {"e_id":"1","e_name":"1","gen":"1","addr":"1"},
        {"e_id":"2","e_name":"2","gen":"2","addr":"2"},
        {"e_id":"3","e_name":"3","gen":"3","addr":"3"}
    ]
    return render_template("forw.html",a=a,b=b,c=c)

@app.route('/emp')
def emp():
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor() 
    sql="""
        select 
            e_id,e_name,gen,addr
        from
             emp
    """
    rs = cs.execute(sql)
    a=[]
    for i in rs:
        a.append(i)

    cs.close()
    conn.close()
    return render_template("emp.html",a=a)

if __name__ == '__main__':
    app.run(debug=True)