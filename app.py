from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
