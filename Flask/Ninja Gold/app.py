from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html', gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    try:
        building = request.form['building']
        if building == 'farm':
            gold_earned = random.randint(10, 20)
        elif building == 'cave':
            gold_earned = random.randint(5, 10)
        elif building == 'house':
            gold_earned = random.randint(2, 5)
        elif building == 'casino':
            gold_earned = random.randint(-50, 50)
        
        session['gold'] += gold_earned
        
        now = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if gold_earned >= 0:
            activity = f"Earned {gold_earned} golds from the {building}! ({now})"
        else:
            activity = f"Entered a casino and lost {abs(gold_earned)} golds... Ouch. ({now})"
        
        session['activities'].append(activity)
    except Exception as e:
        app.logger.error(f"Error processing money: {e}")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
