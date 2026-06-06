from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime
import os

app = Flask(__name__)

CSV_FILE = 'login_data.csv'

# Initialize CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username', 'Email', 'Password', 'Timestamp'])

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save to CSV
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, email, password, timestamp])
        
        return redirect('/success')
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True, port=5001)

