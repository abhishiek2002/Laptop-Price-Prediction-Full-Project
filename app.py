from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/project')
def project():
    return render_template('Project.html')



if __name__ == '__main__':
    app.run(debug=True)