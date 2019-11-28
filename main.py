from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    author = "Ronnie Joshua"
    return render_template('index.html', author=author)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
