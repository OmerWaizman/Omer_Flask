import json
import requests
import random
from flask import Flask, redirect, url_for, request, Blueprint, jsonify
from flask import render_template, session
from mysqlx.protobuf.mysqlx_resultset_pb2 import JSON
import asyncio
import aiohttp
from pages.Assignment10.Assignment10 import Assignment10
from interact_with_DB import interact_db
app = Flask(__name__)
app.register_blueprint(Assignment10)
app.secret_key = '123'
from flask import jsonify


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/assignment8')
def assignment8_page():
    return render_template('Assignment8.html', name='Omer Waizman' , sport1='football' ,sport2='runing' , prog='puyton' , prog2='JAVA', shows=('sainfeld' , 'how i met your mother' , 'suits' , 'survivor' , 'peaky blinders' , '24'))

@app.route('/header')
def header_page():
    return render_template('Header.html')

users = {'user1': {'name': 'Michael:', 'email':'Michael@gmail.com'},
             'user2':{'name': 'Ido:', 'email':'Ido@gmail.com'},
             'user3': {'name': 'Roni:', 'email': 'Roni@gmail.com'},
             'user4': {'name': 'Omer:', 'email': 'Omer@gmail.com'},
             'user5': {'name': 'Gil:', 'email': 'Gil@gmail.com'}}

@app.route('/assignment9', methods=['GET','POST'])
def search_9():



    if request.method == 'GET':
        if 'name' in request.args and 'email' in request.args and 'is_submit' in request.args:
            name = request.args['name']
            email = request.args['email']
            is_submit = request.args['is_submit']


            for value in users.values():
                if(value.get("name") == name and value.get("email") == email):
                    return render_template('Assignment9.html', name=name, email=email)


            if(is_submit):
                return render_template('Assignment9.html', users=users)
        return render_template('Assignment9.html')


    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if 'username' in request.form:
            session['username'] = username
            return render_template('Assignment9.html', username=username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('Assignment9.html')


@app.route('/assignment11/outer_source')
def assignment11_def():
    return render_template('assignment11.html')
@app.route('/assignment11/outer_source/json')
def assignment11_def_json():
    number = request.args['number']
    res = requests.get("https://reqres.in/api/users/{}".format(number))
    response = jsonify(res.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/assignment11/users')
def assignment11_users_def():
        query = 'select  id,name,email from users;'
        users = interact_db(query=query, query_type='fetch')
        response = []
        for user in users:
            response.append({
                "id": user[0],
                "name": user[1],
                "email": user[2]
            })
        return jsonify(users)
        #return render_template('users.html', users=json.dumps(response))



@app.route('/db_users/<int:user_id>')
@app.route('/assignment12/restapi/', defaults={'user_id':1})
@app.route('/assignment12/restapi/<int:user_id>')
def get_users_def(user_id):
    query = 'select  id,name,email from users where id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    user_dict = {
        f'id': users[0].id,
        'name': users[0].name,
        'email': users[0].email
    }
    if len(users) == 0 :
        user_dict = {
            'status' : 'failed' ,
            'message' : 'user not found'
        }
    else:
        user_dict = {
            'status': 'success',
            f'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email
        }
    return jsonify(user_dict)


if __name__ == '__main__':
    app.run(debug=True)
