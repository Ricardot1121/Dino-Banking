# ================================
# DINO BANKING - Main Application
# ================================

# Import Flask and tools we need
from flask import Flask, render_template, request, redirect, url_for

# Create our Flask application
app = Flask(__name__)

# Homepage redirects to login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get what user typed
        username = request.form['username']
        password = request.form['password']
        # Checking everything works
        print(f"Username: {username}, Password: {password}")
        return 'Login successful!'
    return render_template('login.html')

# This ALWAYS goes last - runs the application
if __name__ == '__main__':
    app.run(debug=True)