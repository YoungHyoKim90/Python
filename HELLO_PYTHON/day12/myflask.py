import cx_Oracle

from flask.app import Flask
from flask.globals import request
from flask.templating import render_template
from day12.dao_mem import DaoMem


app = Flask(__name__)


@app.route('/')
@app.route('/mem_list')
def mem_list():
    dm = DaoMem()
    list = dm.select_list()
    return render_template("mem_list.html", list=list)

@app.route('/mem_detail')
def mem_detail():
    m_id = request.args.get('m_id')
    dm = DaoMem()
    mem = dm.select_one(m_id)
    
    return render_template("mem_detail.html", mem=mem)

@app.route('/mem_mod')
def mem_mod():
    m_id = request.args.get('m_id')
    dm = DaoMem()
    mem = dm.select_one(m_id)
    return render_template("mem_mod.html", mem=mem)

@app.route('/mem_mod_act', methods=['POST'])
def mem_mod_act():
   
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    address = request.form['address']

    dm = DaoMem()
    cnt = dm.update(m_id, m_nm, tel, address)

    return render_template("mem_mod_act.html", cnt=cnt, m_id=m_id)

@app.route('/mem_add')
def mem_add():
    return render_template("mem_add.html")


@app.route('/mem_add_act', methods=['POST'])
def mem_add_act():
   
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    address = request.form['address']

    dm = DaoMem()
    cnt = dm.insert(m_id, m_nm, tel, address)

    return render_template("mem_add_act.html", cnt=cnt)


@app.route('/mem_del_act', methods=['POST'])
def mem_del_act():
    m_id = request.form['m_id']
    dm = DaoMem()
    cnt = dm.delete(m_id)
    return render_template("mem_del_act.html", cnt=cnt)


if __name__ == '__main__':
    app.run(debug=True)
    
