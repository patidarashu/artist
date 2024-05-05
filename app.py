from flask import Flask, render_template, request, redirect
app = Flask(__name__)

app.secret_key = 'your_secret_key_here'  # Set a secret key for session management

# Sample user data (in a real application, this would be stored in a database)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/mehndi')
def mehndi():
    return render_template('mehndi.html')

@app.route('/makeup')
def makeup():
    return render_template('makeup.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username in users and users[username] == password:
#             session['username'] = username  # Store the username in the session
#             return redirect('/')
#         else:
#             return render_template('login.html', error='Invalid username or password')
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username not in users:
#             users[username] = password  # Store the new user in the users dictionary
#             return redirect('/login')
#         else:
#             return render_template('signup.html', error='Username already exists')
#     return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
