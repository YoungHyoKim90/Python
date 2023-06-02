from flask import Flask,request, render_template
import cx_Oracle
from day11.dao_emp import DaoEmp
app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.select_list()
    print(list);
    return render_template("emp_list.html",list=list)


@app.route('/emp_detail')
def emp_detail():
    e_id =request.args.get('e_id')
    print("e_id",e_id)
    de = DaoEmp()
    emp = de.select_one(e_id)
    print(emp)
    return render_template("emp_detail.html",emp=emp)

@app.route('/emp_mod')
def emp_mod():
    e_id =request.args.get('e_id')
    de = DaoEmp()
    emp= de.select_one(e_id)
    return render_template("emp_mod.html",emp=emp)

@app.route('/emp_mod_act',methods=['POST'])
def emp_mod_act():
    e_id =request.form.get('e_id')
    e_name =request.form.get('e_name')
    gen =request.form.get('gen')
    addr =request.form.get('addr')
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    
    return render_template("emp_mod_act.html", cnt=cnt)



if __name__ == '__main__':
    app.run(debug=True)
    
  