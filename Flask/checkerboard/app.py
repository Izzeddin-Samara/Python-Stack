from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:cols>')
@app.route('/<int:rows>/<int:cols>')
def checkerboard(rows=8, cols=8):
    return render_template('index.html', rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)
