from flask import Flask,jsonify
from flask.globals import request
from flask.templating import render_template
from day14.dao_emp import DaoEmp
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data['id'])
    return jsonify(result = "success")
    
@app.route('/emp_list.ajax', methods=['POST'])
def ajax_emp_list():
    de = DaoEmp()
    list = de.select_list()
    return jsonify(list = list)

@app.route('/emp_detail.ajax', methods=['POST'])
def ajax_emp_detail():
    param = request.get_json()
    e_id = param['e_id']
    de = DaoEmp()
    emp = de.select_one(e_id)
    return jsonify(emp = emp)
    
@app.route('/emp_add.ajax', methods=['POST'])
def ajax_emp_add():
    param = request.get_json()
    e_id = param['e_id']
    e_name = param['e_name']
    gen = param['gen']
    addr = param['addr']
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return jsonify(cnt = cnt)    

@app.route('/emp_mod.ajax', methods=['POST'])
def ajax_emp_mod():
    param = request.get_json()
    e_id = param['e_id']
    e_name = param['e_name']
    gen = param['gen']
    addr = param['addr']
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return jsonify(cnt = cnt)   

@app.route('/emp_del.ajax', methods=['POST'])
def ajax_emp_del():
    param = request.get_json()
    e_id = param['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    return jsonify(cnt = cnt)
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    