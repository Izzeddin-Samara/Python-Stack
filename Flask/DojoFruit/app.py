from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    strawberry = int(request.form.get('strawberry', 0))
    raspberry = int(request.form.get('raspberry', 0))
    apple = int(request.form.get('apple', 0))
    name = request.form.get('name', '')
    student_id = request.form.get('student_id', '')
    
    total_items = strawberry + raspberry + apple
    order_time = datetime.now().strftime('%B %d %Y %I:%M:%S %p')

    return render_template('checkout.html', strawberry=strawberry, raspberry=raspberry, apple=apple, 
                           name=name, student_id=student_id, total_items=total_items, order_time=order_time)

if __name__ == '__main__':
    app.run(debug=True)
