import hashlib, base64, os
import flask
from flask import Flask,redirect,render_template,request
import sqlite3
from sqlite3 import Error
app = flask.Flask(__name__)
app.config['DEBUG'] = True
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")
        print(path)
    return connection
@app.route('/shortner',methods=['GET'])
def take_url():
    if 'url' in request.args:
        url = str(request.args['url'])
        db = os.getcwd()+'data.sqlite'
        conn =create_connection(db)
        new_url=insert_in_db(conn,url)
        return "{}".format(URL+'shortner/'+str(new_url))
    else:
        return "Please provide a url."
@app.route('/shortner/<key>',methods=['GET'])
def home(key):
    db = os.getcwd()+'data.sqlite'
    conn = create_connection(db)
    ret=find_in_db(conn,str(key))
    if ret =='':
        return 'Not Found'
    else:
        return redirect('https://'+ret)

def generate_key(url):
    text_utf8 = url.encode('utf8')
    sha256 = hashlib.sha256(text_utf8).digest()
    b64 = base64.b64encode(sha256)
    return b64.decode('utf-8')

def insert_in_db(conn,url):
    try:
        c = conn.cursor()
        sql='''
        INSERT INTO data(key,url) VALUES(?,?) 
        '''
        key=generate_key(url)
        values=(key,url)
        c.execute(sql,values)
        conn.commit()
        return key
    except Exception as e:
        print(e)
def find_in_db(conn,key):
    try:
        c = conn.cursor()
        sql='''
        SELECT url from data where key=?
        '''
        c.execute(sql,(key,))
        rows = c.fetchall()
        if len(rows)==0:
            return ''
        else:
            return rows[0][0]
    except Exception as e:
        print(e)
def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

create_table_sql = '''
CREATE TABLE IF NOT EXISTS data(
    key text PRIMARY KEY,
    url text NOT NULL
);
'''
URL = 'localhost:5000/'

if __name__=='__main__':
    db = os.getcwd()+'data.sqlite'
    conn = create_connection(db)    
    if conn is not None:
        create_table(conn,create_table_sql)
    else:
        print("can't establish connection to db")
    conn.close()
    app.run(port=5000)