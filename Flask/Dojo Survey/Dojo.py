from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    location = request.form.get('location')
    language = request.form.get('language')
    comment = request.form.get('comment')
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
