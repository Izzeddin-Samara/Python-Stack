from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/play/')
@app.route('/play/<int:num_boxes>/')
@app.route('/play/<int:num_boxes>/<color>')
def play(num_boxes=3, color="#9fc5f8"):
    return render_template('index.html', num_boxes=num_boxes, box_color=color)

if __name__ == '__main__':
    app.run(debug=True)
