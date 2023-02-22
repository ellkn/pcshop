from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TOPSECRETKEY'


@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return render_template('error.html')


if __name__ == '__main__':
   app.run(debug = True)