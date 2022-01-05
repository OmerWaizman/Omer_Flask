from flask import Flask, redirect, url_for, request, Blueprint
from flask import render_template, session
from pages.assignment10.assignment10 import assignment10
from interact_with_DB import interact_db
app = Flask(__name__)
app.register_blueprint(assignment10)
app.secret_key = '123'



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





if __name__ == '__main__':
    app.run(debug=True)








# @app.route('/users')
# def users_page():
# query = 'select * from users':
# users = interact_with_DB(query=query, query_type='fetch')
# return render_template('users.html', users='users')